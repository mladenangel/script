from colorama import *
try:
    a=18
    b=0
    c=a/b
    print(Fore.RED+Back.YELLOW+str(c)+Style.RESET_ALL)
except Exception as e:
    print(Fore.YELLOW+Back.RED+str(e))
finally:
    print(Fore.RED+Back.YELLOW+'Done')
print(Fore.RED+Back.YELLOW+'Exit'+Style.RESET_ALL)

