from colorama import *
print(Fore.RED+Back.YELLOW+'Creating File'+Style.RESET_ALL)
file1 = open('DOC1','a')
print(Fore.GREEN+Back.WHITE+'Writing data into file..')
for i in range(1,11):
    name='user'+str(i-1)
    email='user'+str(i-1)+'@email.com'
    data = '{} {} {}\n'.format(str(i),name,email)
    print(Fore.BLUE+Back.WHITE+data+Style.RESET_ALL)
    file1.write(data)
print(Fore.RED+Back.YELLOW+'Closing file...'+Style.RESET_ALL)
file1.close()

