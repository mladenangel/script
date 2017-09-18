#!/usr/bin/env python3
#delwin
import socket
from colorama import *

def conv_int():
    data = input(Fore.RED+Back.WHITE+'data?:'+Style.RESET_ALL)
    #32 bit
    print(Fore.BLUE+Back.WHITE+'Original:%s=>Long host byte order:%s=>Net byte order:%s' %(data,socket.ntohl(int(data)),socket.htonl(int(data))))
    #16 bit
    print('Original:%s=>Short host byte order:%s => Net byte order:%s' %(data,socket.ntohs(int(data)),socket.htons(int(data)))+Style.RESET_ALL)

if __name__=='__main__':
    conv_int()
