#!/usr/bin/env python3
# mladen angelov 2017 sep 14 15:50

from colorama import *
import time
import random
from random import randrange


class SearchAndDestroy:
    def __init__(self,msg,soup,result):
        self.msg = msg
        self.soup = soup
        self.result = result

    def search(msg,soup,result):
        for i in range(len(msg)):
            if msg[i] in soup:
                result.append(msg[i])
                i += 1
            else:
                print(Fore.YELLOW+Back.RED+'False: %s' %(msg)+Style.RESET_ALL)
                break
        return result

m = int(input('Size of Soup:?'))
n = int(input('Size of Msg:?'))

    
result = []
for listSize in range(m):
    m = time.time()
    for msgSize in range(n):
        msg = [randrange(100000) for x in range(listSize)]
        soup = [randrange(100000) for x in range(listSize)]
        start = time.time()
        SearchAndDestroy.search(msg,soup,result)
        print('I write this:%s' %(result))
        end = time.time()
        print(Fore.RED+Back.YELLOW+'size:%d time:%f' %(listSize,end-start)+Style.RESET_ALL)
n = time.time()
print(Fore.RED+Back.WHITE+'start time:%s, end time:%s' %(m,n)+Style.RESET_ALL)

