#!/bin/usr/python3

# Script Name:                  ops401-challenge02
# Author:                       Omar Ardid
# Date of latest revision:      04/30/2024
# Purpose:                      Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

import os 

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
ip_address = input("Enter an ip address: ")
result = os.system(f'ping {ip_address} -c 2')

# Get the current timestamp
from datetime import datetime
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
if result == 0:
    status = "Success"
    print(f"{timestamp} Destination IP: {ip_address} Lan is up and running! ")
else:
    status = "Failure"
    print(f"{timestamp} Destination IP: {ip_address} Lan is down!")

print(f"Status: {status}")