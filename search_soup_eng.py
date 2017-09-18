#!/usr/bin/env python3
# mladen angelov 2017 sep 14 15:50


from colorama import *

msg = input(Fore.RED+Back.YELLOW+'What msg you wont to write?:'+Style.RESET_ALL)
soup =input(Fore.YELLOW+Back.RED+'Soup(collecton of letters) for this msg?:'+Style.RESET_ALL)

result = []

class SearchAndDestroy:
    def __init__(self,msg,soup,result):
        self.msg = msg
        self.soup = soup
        self.result = result

    def Search(msg,soup,result):
        for i in range(len(msg)):
            if msg[i] in soup:
                result.append(msg[i])
                i += 1
            else:
                print(Fore.YELLOW+Back.RED+'I cant write this!: %s' %(msg)+Style.RESET_ALL)
                break
        return result


    
if __name__=='__main__':
    SearchAndDestroy.Search(msg,soup,result)
    print(Fore.RED+Back.YELLOW+'I write this:%s' %(result)+Style.RESET_ALL)
