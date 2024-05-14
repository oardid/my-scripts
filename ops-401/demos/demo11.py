#!bin/bash/env python3

# import scapy.all as scapy
from scapy.all import Ether, ARP, IP, sniff, sr1, ICMP

request = sr1(IP(dst='scanme.nmap.org') / ICMP())

if request:
    print(request.show())
#my_frame = Ether() / ARP()

#print(my_frame)
#print('-' * 80)
#print(my_frame.show())
#print('-' * 80)
#print(my_frame.dst)

#packets = scapy.sniff(count=10)

#print(packets[0].dst)
# for _ in packets:
#   num = 0
#   pritn(packets[num].show())


host = 'scanme.namp.org'
port_range = 22
src_port = 22
dst_port = 22

#response - srl(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='s'), timeout=1, verbose=0)