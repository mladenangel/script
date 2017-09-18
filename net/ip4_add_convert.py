#!/usr/bin/env python3
# delwin

from colorama import *
import socket
from binascii import hexlify

def conver_ip_ass():
    a = input(Fore.BLUE+Back.WHITE+'IP ass?:'+Style.RESET_ALL)
    for ip_ass in [a]:
        packed_ip = socket.inet_aton(ip_ass)
        unpacked_ip = socket.inet_ntoa(packed_ip)
        print(Fore.BLUE+Back.WHITE+'IP Asses Packed:,Unpacked:',ip_ass,'',hexlify(packed_ip),unpacked_ip+Style.RESET_ALL)
if  __name__ == '__main__':
    conver_ip_ass()
