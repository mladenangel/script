import colorama
from colorama import Fore, Back, Style

colorama.init()
message = 'Hello world from python'
str1 = 'DELWIN'
str2= 'THE BEST'
print(message)
print(Fore.RED+Back.WHITE+message+Style.RESET_ALL)
print(Fore.YELLOW+message)
print(Fore.RED + message)
print(Fore.GREEN + message)
print(Fore.BLUE + message)
print(Fore.RED+Back.YELLOW+message+Style.RESET_ALL)
print(Fore.RED+Back.WHITE+"%s %s" %(str1,str2)+Style.RESET_ALL)

