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

# Ask the user for an email address and password to use for sending notifications.
email = input("Enter your email address: ")
password = getpass("Enter your pasword: ")
recipient = input("Enter the recipient's email address: ")

# Function to send an email notification
def send_email(subject, message):
    try:
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
        print(f"Email sent to {recipient} has been successful!")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

# Test email sending before the loop
send_email("Test Email", "This is a test email to check if sending works.")

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
ip_address = input("Enter an IP address to transmit a single ICMP packet to: ")

# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
pings = 0 
prevstatus = None
while True:
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Execute ping command to get the current status
    result = os.system(f'ping -c 1 {ip_address} > /dev/null 2>&1')
    
    if result == 0:
        status = "Success"
        print(f"{timestamp} Network {status} to {ip_address} Lan is up and running!") 
        if prevstatus == "Failure":
            send_email("Network Status Changed", f"Network status changed from {prevstatus} to {status} at {timestamp}")
        prevstatus = status
    else:
        status = "Failure"
        print(f"{timestamp} Network {status} to {ip_address} Lan is down!")
        if prevstatus == "Success":
            send_email("Network Status Changed", f"Network status changed from {prevstatus} to {status} at {timestamp}")
        prevstatus = status
    time.sleep(2)    
    pings += 1
    if pings >= 4:
        break
