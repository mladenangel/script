#!/usr/bin/env python3
# delwin

from colorama import *
import socket

def remote_machine():
    remote_host = input(Fore.RED+Back.YELLOW+'Remote host name ?:'+Style.RESET_ALL)
    remote_ip = socket.gethostbyname(str(remote_host))
    print(Fore.BLUE+Back.WHITE+remote_host,'have IP:',remote_ip+Style.RESET_ALL)
    

if __name__ == '__main__':
    remote_machine() 
