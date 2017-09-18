# simple database
# delwin

from colorama import *

people = {
    'delwin':{
        'phone':'697583458','addr':'Jaboneros 7'
    },
    'joe':{
        'phone':'698456783','addr':'Bar steet 4'
    },
    'mladen':{
        'phone':'456333211','addr':'Delwin streer 3'
    }
}

labels = {'phone':'phone number','addr':'address'}

name = str(input(Fore.RED+Back.YELLOW+'Name:'+Style.RESET_ALL))

request = str(input('Phone number(p) or address(a)?'))

if request == 'p':key = 'phone'
if request == 'a':key = 'addr'

if name in people:print(Fore.RED+Back.WHITE+"%s's %s is %s."%(name,labels[key], people[name][key])+Style.RESET_ALL)

