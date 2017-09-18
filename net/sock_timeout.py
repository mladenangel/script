#!/usr/bin/env python3
#delwin

import socket
from colorama import *

def sock_timeout():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(Fore.BLUE+Back.WHITE+'Default sock timeout:%s' %s.gettimeout())
    s.settimeout(100)
    print('Current sock timeout:%s' %s.gettimeout()+Style.RESET_ALL)
if __name__=='__main__':
    sock_timeout()
