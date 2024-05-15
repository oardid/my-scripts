#!/bin/usr/python3

# Script Name:                  ops401-challenge13
# Author:                       Omar Ardid
# Date of latest revision:      05/15/2024
# Purpose:                      Combining port and ping mode 
# Resources:                    

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

# Prompt the user for target IP address
target_ip = input("Enter the target IP address or network (e.g., 192.168.1.1 or 192.168.1.0/24): ")

# Example usage
icmp_ping_and_scan(target_ip, [22, 80, 443, 3389])
