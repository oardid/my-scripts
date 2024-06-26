#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) OS Detection\n""")

ports = input("Enter the port range (e.g. 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, ports, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    scanner.scan(ip_addr, ports, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    scanner.scan(ip_addr, ports, '-v -O')
    print(scanner.scaninfo())
    print(scanner[ip_addr])
    if 'osclass' in scanner[ip_addr]:
        for osclass in scanner[ip_addr]['osclass']:
            print(f"The OS of {ip_addr} is {osclass['osfamily']} {osclass['osgen']}")
    else:
        print("No OS information available.")
else:
    print("Please enter a valid option")
