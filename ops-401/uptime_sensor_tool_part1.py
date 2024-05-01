#!/bin/usr/python3

# Script Name:                  ops401-challenge02
# Author:                       Omar Ardid
# Date of latest revision:      04/30/2024
# Purpose:                      Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

import os 
import time
from datetime import datetime

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
ip_address = input("Enter an ip address: ")
result = os.system(f'ping -c 1 {ip_address} > /dev/null 2>&1')

# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
pings = 0 
while True:
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if result == 0:
        status = "Success"
        print(f"{timestamp} Network {status} to {ip_address} Lan is up and running! ")
        time.sleep(2)
    else:
        status = "Failure"
        print(f"{timestamp} Network {status} to {ip_address} Lan is down!")
        time.sleep(2)
    pings += 1
    if pings >= 4:
        break