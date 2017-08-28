import colorama
from colorama import *

print(Fore.RED+Back.YELLOW+'Creating files...'+Style.RESET_ALL)
#if file is existing, it erases and creates a new one
f1 = open('mydoc1','w')
#if file is existing, it appends.Otherwise,it creates
f2 = open('mydoc2','a')
#binary files
bf1 = open('mydoc3','wb')
bf2 = open('mydoc4','ab')
#writing data
print(Fore.YELLOW+Back.RED+'Writing data into files...'+Style.RESET_ALL)
for index in range(1,10):
    data = ''
    name ='user'+str(index-1)
    email='user'+str(index-1)+'@email.com'
    data = '{} {} {}\n'.format(str(index-1),name,email)
    f1.write(data)
    f2.write(data)
print(Fore.BLUE+Back.WHITE+'Close files...'+Style.RESET_ALL)
f1.close()
f2.close()
bf1.close()
bf2.close()

