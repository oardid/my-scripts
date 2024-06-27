#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5  # Set a timeout value here in seconds
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ")
portno = int(input("Enter the port number: "))

def portScanner(portno):
    try:
        sockmod.connect((hostip, portno))
        print("Port", portno, "is open")
    except:
        print("Port", portno, "is closed")

portScanner(portno)