#!/usr/bin/env python3
# delwin

import socket
from colorama import *

def find_service():
    a = input(Fore.RED+Back.WHITE+'PORT ?:'+Style.RESET_ALL)
    if a == 53:
        protocol='udp'
    else:
        protocol='tcp'
    for port in [int(a)]:
        print(Fore.RED+Back.YELLOW+'Port:%s Service name:%s' %(port,socket.getservbyport(port,protocol))+Style.RESET_ALL)
if __name__=='__main__':
    find_service()
