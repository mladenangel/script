#!/usr/bin/env python
# delwin

from colorama import *
x = 'What is the Matrix ?'.find('Matrix')
if x ==  12:
    print(Fore.RED+Back.YELLOW+'Matrix is: %s'%(x)+Style.RESET_ALL)
else:
    print(Fore.YELLOW+Back.RED+'What is the Matrix?'+Style.RESET_ALL)
