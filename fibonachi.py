#!/usr/bin/env python3
# delwin

from colorama import *

fibs = [0,1]
num = input(Fore.BLUE+Back.WHITE+'How many Fibonacci numbers do you want?'+Style.RESET_ALL)
if num == (0):
    print(Fore.RED+Back.YELLOW+'Wrong number !!!'+Style.RESET_ALL)
else:
    for i in range(num-2):
        fibs.append(fibs[-2]+fibs[-1])
    print(Fore.RED+Back.WHITE+'Your fibonacci numbers:%s'%fibs+Style.RESET_ALL)
