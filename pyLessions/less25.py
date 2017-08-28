import colorama
from colorama import *
msg='delwin'
for i in msg:
    print(Fore.YELLOW+Back.RED+i+Style.RESET_ALL)
for i in msg:
    print(Fore.RED+Back.YELLOW+i.upper()+Style.RESET_ALL)
for i in msg:
    print(Fore.YELLOW+Back.RED+i.lower()+Style.RESET_ALL)

