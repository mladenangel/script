import sys
from colorama import *

print(Fore.RED+Back.WHITE+'Openig file...')

file = open('DOC1','r')
def reading_data(f):
    while True:
        data = f.readline()
        if (data=='')or(data==None):
            break
        sys.stdout.write(data)
print(Fore.BLUE+Back.WHITE+'For DOC1>>>>>>')
reading_data(file)
print(Fore.RED+'End'+Style.RESET_ALL)
print(Fore.RED+Back.WHITE+'Close file...'+Style.RESET_ALL)
file.close()
