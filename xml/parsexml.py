# delwin


from colorama import *
import xml.etree.cElementTree as ET

print(Fore.RED+Back.WHITE+'Simple XML parser'+Style.RESET_ALL)
tree = ET.ElementTree(file='test.xml')
root = tree.getroot()
print(Fore.RED+Back.YELLOW+'From test.xml file:'+Style.RESET_ALL)
print(Fore.BLUE+Back.WHITE+'Root tag: %s' %(root.tag))
print('Root attrib: %s' %(root.attrib)+Style.RESET_ALL)

for child_of_root in root:
    print(Fore.RED+Back.YELLOW+'Child Tags: %s' %(child_of_root.tag)+Style.RESET_ALL)
    print(Fore.YELLOW+Back.RED+'Child Atrrib: %s' %(child_of_root.attrib)+Style.RESET_ALL)




