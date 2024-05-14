#!/bin/usr/python3

# Script Name:                  ops401-challenge11
# Author:                       Omar Ardid
# Date of latest revision:      05/13/2024
# Purpose:                      Creating a TCP Port Range Scanner that tests whether a TCP port is open or closed.
# Resources:                    https://denizhalil.com/2023/11/14/python-port-scanning-banner-retrieval/ https://denizhalil.com/2023/11/13/port-scanning-with-scapy/

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1, send

# Grabing user input for host IP and port range
print("Before running the script, make sure to run as Super User 'sudo, su'")
target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port range: "))
end_port = int(input("Enter the ending port range: "))

def scan_port(target_ip, port):
    # Creating an IP packet with TCP layer
    ip_pkt = IP(dst=target_ip)
    tcp_pkt = TCP(dport=port, flags="S")
    # Sending the packet and receiving a response
    response = sr1(ip_pkt/tcp_pkt, timeout=1, verbose=0)
    if response:
        # Checking the flags in response
        if response.haslayer(TCP):
            flags = response.getlayer(TCP).flags
            # Checking if flasg is set to 0x12
            if flags == 0x12: #SYN-ACK check
                send(ip_pkt/TCP(dport=port, flags="R"), verbose=0)
                print(f"Port {port} is open")
            # Checking if flasg is set to 0x14
            elif flags == 0x14: # RST-ACK check
                print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered and silently dropped")
    else:
        print(f"Port {port} is filtered and silently dropped")

# Looping through each range port and scaning each one
for port in range(start_port, end_port + 1):
    scan_port(target_ip, port)