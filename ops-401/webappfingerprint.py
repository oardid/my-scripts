#!/usr/bin/python3

# Script Name:                  ops401-challenge36
# Author:                       Omar Ardid
# Date of latest revision:      06/17/2024
# Purpose:                      Creating a script that utilizes multiple banner grabbing approaches against a single target.
# Resources:                    https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/

import os, time, socket, subprocess

def banner_grabbing_netcat(url, port):
    """
    This function uses the netcat command to connect to a target URL and port, and then sends a HEAD request to retrieve the server banner.

    :param url: The target URL or IP address
    :param port: The target port number
    :return: None
    """
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Set a timeout for the connection (30 seconds)
        s.settimeout(30)
        # Connect to the target URL and port
        s.connect((url, int(port)))
        # Send a HEAD request to retrieve the server banner
        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        # Wait for 1 second to allow the server to respond
        time.sleep(1)
        # Receive the server banner and print it
        banner = s.recv(1024).decode()
        print(f"Netcat Banner Grab: {banner}")
        # Close the socket
        s.close()

def banner_grabbing_telnet(url, port):
    """
    This function uses the telnet command to connect to a target URL and port, and then sends a HEAD request to retrieve the server banner.

    :param url: The target URL or IP address
    :param port: The target port number
    :return: None
    """
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Set a timeout for the connection (30 seconds)
        s.settimeout(30)
        # Connect to the target URL and port
        s.connect((url, int(port)))
        # Send a HEAD request to retrieve the server banner
        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        # Wait for 1 second to allow the server to respond
        time.sleep(1)
        # Receive the server banner and print it
        banner = s.recv(1024).decode()
        print(f"Telnet Banner Grab: {banner}")
        # Close the socket
        s.close()

def banner_grabbing_nmap(target):
    """
    This function uses the Nmap command-line tool to scan a target IP address or hostname for open ports and retrieve banners for those ports.

    :param target: The target IP address or hostname
    :return: None
    """
    try:
        print(f"Running Nmap on {target}")
        # Run Nmap with the -sS option (TCP SYN scan) and save the output to a variable
        command = ["nmap", "-sS", target]
        output = subprocess.check_output(command)
        nmap_output = output.decode('utf-8')
        print(f"Nmap output: {nmap_output}")

        for line in nmap_output.split('\n'):
            if 'open' in line and 'tcp' in line:
                try:
                    # Extract the port number from the Nmap output
                    parts = line.split(' ')
                    port = parts[-1].split('/')[0]
                    if port.isdigit():
                        port = int(port)
                        # Create a socket object and connect to the target port
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((target, int(port)))
                        # Send a HEAD request to retrieve the server banner
                        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                        time.sleep(1)  # Wait for 1 second
                        # Receive and print the server banner
                        banner = s.recv(1024).decode()
                        print(f"Nmap Banner Grab: {target} - Port {port} - {banner}")
                        s.close()
                except Exception as e:
                    print(f"Error: {e}")
    except Exception as e:
        print(f"(ง •̀_•́)ง Error: {e}")

def main():
    url = input("Enter a URL or IP address of a web server: ")
    port = input("Enter a port number you want to scan the web server: ")

    print("\nPerforming Netcat Banner Grab... ʕ•́ᴥ•̀ʔっ")
    banner_grabbing_netcat(url, port)

    print("Performing Telnet Banner Grab... ʕ•́ᴥ•̀ʔっ")
    banner_grabbing_telnet(url, port)

    print("Performing Nmap Banner Grab... ʕ•́ᴥ•̀ʔっ")
    banner_grabbing_nmap(url)

if __name__ == "__main__":
    main()