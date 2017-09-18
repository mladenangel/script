#!/usr/bin/env python3
# delwin

from colorama import *

msg = input(Fore.RED+Back.YELLOW+'Que quere escribir?:'+Style.RESET_ALL)
soup =input(Fore.YELLOW+Back.RED+'Con que soup(colection de letras) quere escribir?:'+Style.RESET_ALL)

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
                print(Fore.YELLOW+Back.RED+'No es posible! escribir: %s' %(msg)+Style.RESET_ALL)
                break
        return result


    
if __name__=='__main__':
    SearchAndDestroy.Search(msg,soup,result)
    print(Fore.RED+Back.YELLOW+'Resultato posible para escribir:%s' %(result)+Style.RESET_ALL)
