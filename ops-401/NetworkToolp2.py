#!/bin/usr/python3

# Script Name:                  ops401-challenge12
# Author:                       Omar Ardid
# Date of latest revision:      05/14/2024
# Purpose:                      Adding more features to Network Security Tool
# Resources:                    https://denizhalil.com/2023/11/14/python-port-scanning-banner-retrieval/ https://denizhalil.com/2023/11/13/port-scanning-with-scapy/

from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1, send
import ipaddress
import logging

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
    except Exception as e:
        print(f"An error occurred while scanning port {port}: {e}")

# Peform ICMP ping sweep on a network    
def icmp_ping(network):
    online_count = 0
    # Create an IP network variable
    network_address = ipaddress.ip_network(network, strict=False)
    for ip in network_address.hosts():
        ip = str(ip)
        # Run through each host in the network (excluding network and broadcast addresses)
        if ipaddress.ip_address(ip) in [network_address.network_address, network_address.broadcast_address]:
            continue
        # Creating ICMP packet and sending it 
        pkt = IP(dst=ip) / ICMP()
        resp = sr1(pkt, timeout=0.1, verbose=0)
        # Check reponse 
        if resp is None:
            print(f"Host {ip} is down or unresponsive.")
        elif resp.haslayer(ICMP) and resp[ICMP].type == 3 and resp[ICMP].code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {ip} is actively blocking ICMP traffic.")
            online_count += 1
        else:
            print(f"Host {ip} is responding.")
            online_count += 1
    # Print the total number of online hosts
    print(f"\n{online_count} hosts are online.")

while True:
    print("\n~~~~~ Network Scanner Tool ~~~~~")
    print("1. TCP Port Range Scanner mode")
    print("2. ICMP Ping Sweep mode")
    print("3. Exit")
    choice = input("Select your choice! ")

    if choice == '1':
        # Grabing user input for host IP and port range
        target_ip = input("Enter the target IP address: ")
        start_port = int(input("Enter the starting port range: "))
        end_port = int(input("Enter the ending port range: "))
        # Looping through each range port and scanning each one
        for port in range(start_port, end_port + 1):
            scan_port(target_ip, port)
    elif choice == '2':
        # Asking the user for network address and perform ICMp ping sweep
        network = input("Enter network address including CIDR block! (Ex: 10.10.0.0/24): ")
        icmp_ping(network)
    elif choice == '3':
        print("Goodbye! :(")
        break
    else:
        # Invalid choice, prompting the user to try again
        print("INVALID CHOICE, TRY AGAIN!!!")
