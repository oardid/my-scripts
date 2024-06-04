#!/bin/usr/python3

# Script Name:                  ops401-challenge26
# Author:                       Omar Ardid
# Date of latest revision:      06/03/2024
# Purpose:                      Adding logs to previous script
# Resources:                    https://dotnettutorials.net/lesson/logging-module-in-python/

from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1, send
import ipaddress
import logging

# Configure logging
logging.basicConfig(filename='port_scanner.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Scan a specific port on a target IP address
def scan_port(target_ip, port):
    try:
        # Create IP and TCP packets
        ip_pkt = IP(dst=target_ip)
        tcp_pkt = TCP(dport=port, flags="S")
        # Send the packet and receive a response
        response = sr1(ip_pkt/tcp_pkt, timeout=0.1, verbose=0)
        if response:
            if response.haslayer(TCP):
                flags = response.getlayer(TCP).flags
                # Check TCP flags in response
                if flags == 0x12:
                    # Port is open
                    send(ip_pkt/TCP(dport=port, flags="R"), verbose=0)
                    logging.info(f"Port {port} on {target_ip} is open")
                elif flags == 0x14:
                    # Port is closed
                    logging.info(f"Port {port} on {target_ip} is closed")
                else:
                    # Port is filtered
                    logging.info(f"Port {port} on {target_ip} is filtered and silently dropped")
        else:
            # No response received
            logging.info(f"Port {port} on {target_ip} is filtered and silently dropped")
    except Exception as e:
        # Exception occurred while scanning port
        logging.error(f"Error scanning port {port} on {target_ip}: {e}")

# Perform ICMP ping sweep on a network and scan open ports on responsive hosts
def icmp_ping_and_scan(target_ip, ports):
    online_count = 0
    if "/" not in target_ip:
        try:
            # Check if the input is a single IP address
            ipaddress.ip_address(target_ip)
        except ValueError:
            # Invalid IP address provided
            logging.error("Invalid IP address provided.")
            return

        # Create ICMP packet and send it
        pkt = IP(dst=target_ip) / ICMP()
        resp = sr1(pkt, timeout=0.1, verbose=0)
        if resp is None:
            # Host is down or unresponsive
            logging.info(f"Host {target_ip} is down or unresponsive.")
            return
        elif resp.haslayer(ICMP) and resp[ICMP].type == 3 and resp[ICMP].code in [1, 2, 3, 9, 10, 13]:
            # Host is actively blocking ICMP traffic
            logging.info(f"Host {target_ip} is actively blocking ICMP traffic.")
            return
        else:
            # Host is responding
            logging.info(f"Host {target_ip} is responding.")
            online_count += 1
            # Scan ports if host is responsive
            for port in ports:
                scan_port(target_ip, port)
    else:
        # Perform ICMP ping sweep on a network
        network_address = ipaddress.ip_network(target_ip, strict=False)
        for ip in network_address.hosts():
            ip = str(ip)
            if ipaddress.ip_address(ip) in [network_address.network_address, network_address.broadcast_address]:
                continue

            # Create ICMP packet and send it
            pkt = IP(dst=ip) / ICMP()
            resp = sr1(pkt, timeout=0.1, verbose=0)
            if resp is None:
                # Host is down or unresponsive
                logging.info(f"Host {ip} is down or unresponsive.")
            elif resp.haslayer(ICMP) and resp[ICMP].type == 3 and resp[ICMP].code in [1, 2, 3, 9, 10, 13]:
                # Host is actively blocking ICMP traffic
                logging.info(f"Host {ip} is actively blocking ICMP traffic.")
            else:
                # Host is responding
                logging.info(f"Host {ip} is responding.")
                online_count += 1
                # Scan ports if host is responsive
                for port in ports:
                    scan_port(ip, port)
    
    # Print the total number of online hosts if it's not a single IP address
    if "/" in target_ip:
        logging.info(f"{online_count} hosts are online.")

# Prompt the user for target IP address
target_ip = input("Enter the target IP address or network (e.g., 192.168.1.1 or 192.168.1.0/24): ")

# Ports scans
icmp_ping_and_scan(target_ip, [22, 80, 443, 3389])
