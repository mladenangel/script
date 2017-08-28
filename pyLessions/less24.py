import colorama
from colorama import *

str1='DELWIN'
str2='THE BEST'
print(Fore.RED+str1+''+str2)
print(Fore.GREEN+str1,str2)
print(Fore.RED+Back.YELLOW+"%s %s" %(str1,str2)+Style.RESET_ALL)
print(Fore.BLACK+Back.WHITE+"{}{}".format(str1,str2)+Style.RESET_ALL)

a='2'
b='6.8'
num1=int(a)
num2=float(b)
print(num1,num2)
print(Fore.GREEN+str(num1))
print(Fore.GREEN+str(num2))
a=2014
b=50000
str1=str(a)
str2=str(b)
print(Fore.RED+Back.WHITE+str1+str2+Style.RESET_ALL)
msg = 'Berlin;Madrid;London;Tokio'
cities = msg.split(';')
for city in cities:
    print(Fore.BLACK+Back.YELLOW+city+Style.RESET_ALL)

msg='tova e edno mnogo dalgo mesegge'
print(Fore.YELLOW+msg)
y=msg[12]+msg[20]+msg[3]+msg[8]+msg[5]+msg[9]
print(Fore.RED+Back.YELLOW + y + Style.RESET_ALL)
print(y[2:])
print(y[:2])
print(y[-3:])
print(y[:-3])
print(y[1:5])
print(y[5:1])
print(y.upper())
print(y.lower())
print(Fore.BLACK+Back.YELLOW+y.upper()+Style.RESET_ALL)
print(Fore.RED+Back.WHITE+y.lower()+Style.RESET_ALL)
str1="Hello word"
str2="From Python"
str3="Y Delwin"

# Zalepva gi
print(Fore.RED+Back.YELLOW+str1+""+str2+''+str3+Style.RESET_ALL)
# Ne gi zalepva
print(Fore.YELLOW+Back.RED+str1,str2,str3+Style.RESET_ALL)
# Ne gi zalepva
print(Fore.BLACK+Back.WHITE+"%s %s %s" %(str1,str2,str3)+Style.RESET_ALL)
#  Ne gi zalepva
print(Fore.WHITE+Back.YELLOW+"{} {} {}".format(str1,str2,str3)+Style.RESET_ALL)
# Zalepva
print(Fore.GREEN+Back.WHITE+"{}{}{}".format(str1,str2,str3)+Style.RESET_ALL)
# Zalepva
print(Fore.YELLOW+Back.GREEN+"%s%s%s" %(str1,str2,str3)+Style.RESET_ALL)

a=6
b=10.34
str1=str(a)
str2=str(b)
print(Fore.RED+Back.GREEN+"%s %s" %(str1,str2)+Style.RESET_ALL)
msg='Berlin;Madrid;Roma;Paris;Sofia'
cities=msg.split(';')
for city in cities:
    print(Fore.YELLOW+Back.RED+city+Style.RESET_ALL)

msg='Delwin is the best when he wont'
print(Fore.RED+Back.YELLOW+msg.upper()+Style.RESET_ALL)
print(Fore.YELLOW+Back.RED+msg.lower()+Style.RESET_ALL)

print(Fore.GREEN+Back.WHITE+msg[5:]+Style.RESET_ALL)
print(Fore.BLUE+Back.WHITE+msg[:6]+Style.RESET_ALL)
print(Fore.RED+Back.WHITE+msg[2:6]+Style.RESET_ALL)
print(Fore.YELLOW+Back.WHITE+msg[0:9]+Style.RESET_ALL)
length=len(msg)
print(Fore.BLACK+Back.WHITE+str(length)+Style.RESET_ALL)



