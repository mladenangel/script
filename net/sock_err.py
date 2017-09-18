#!/usr/bin/env python3
#delwin
import sys
import socket
import argparse
from colorama import *


def main():
    # setup parser
    parser = argparse.ArgumentParser(description='Sock Errors')
    parser.add_argument('--host',action='store',dest='host',required=False)
    parser.add_argument('--port',action='store',dest='port',required=False)
    parser.add_argument('--file',action='store',dest='file',required=False)
    given_args=parser.parse_args()
    host=given_args.host
    port=given_args.port
    file=given_args.file
    # create socket
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error,e:
        print(Fore.RED+Back.WHITE+'Error creating sock:%s'%e+Style.RESET_ALL)
        sys.exit(1)
    #connect
    try:
        s.connect((host,port))
    except socket.error, e:
        print(Fore.RED+Back.WHITE+'Connection error:%s' %e+Style.RESER_ALL)
        sys.exit(1)
    #send data
    try:
        s.sendall('GET %s HTTP/1.0\r\n\r\n' %filename )
    except  socket.error, e:
        print(Fore.RED+Back.WHITE+'Error send data:%s' %e+Style.RESET_ALL)
        sys.exit(1)
    #receive data
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print(Fore.RED+Back.WHITE+'Error receiving data:%s'%e+Style.RESET_ALL)
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)
if __name__=='__main__':
    main()


