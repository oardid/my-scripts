#!/bin/usr/python3

# Script Name:                  ops401-challenge03
# Author:                       Omar Ardid
# Date of latest revision:      05/01/2024
# Purpose:                      Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

import os
import time
import smtplib
from datetime import datetime
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Ask the user for their email address and password
email = input("Please enter your email address: ")
password = getpass("Please enter your password: ")

# Set the recipient email address (administrator)
recipient = input("Enter the recipient's email address: ")

# Function to send an email
def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, recipient, text)
    server.quit()

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
ip_address = input("Enter an ip address to transmit a single ICMP packet to: ")

# Initialize the previous status
prev_status = None
pings = 0 
while True:
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Ping the IP address
    result = os.system(f'ping -c 1 {ip_address} > /dev/null 2>&1')
    
    # Evaluate the response as either success or failure.
    if result == 0:
        status = "Success"
        print(f"{timestamp} Network {status} to {ip_address} Lan is up and running! ")
    else:
        status = "Failure"
        print(f"{timestamp} Network {status} to {ip_address} Lan is down!")
    
    # If the status has changed, send an email
    if status != prev_status:
        send_email(f"Network Status Change for {ip_address}", f"{ip_address} has changed to {status} at {timestamp}.")
    
    # Update the previous status
    prev_status = status
    
    time.sleep(2)
    pings += 1
    if pings >= 4:
        break