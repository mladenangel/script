# delwin

import string
a=string.digits
print(a)
a = string.letters
print(a)
a= string.lowercase
print(a)
a = string.printable
print(a)
a = string.punctuation
print(a)
a= string.uppercase
print(a)
p = 'With a moo-moo here, and a moo-moo there'
d = p.find('moo')
print(d)
seq = ['1','2','3','4','5','6']
sep = '+'
print(sep.join(seq)) #join a list
dir = '','usr','bin','env'
print('/'.join(dir))
print('C:'+'\\'.join(dir))
print(p.lower())
print(p.replace('moo-moo','poo-poo'))
c = '/usr/bin/env'
print('dir: %s' %c)
d = c.split('/')
print('dir split: %s' %d)

c = 'Brain,233,222,444,333,2222,33,222,2'
print('String: %s' %c)
d = c.split(',')
print('Split string into list: %s' %d)

c = 'bshekjlksklmmde.ddmejkjk,jdeijid,dede,deded,dedeeefff'
d = c.split(',')
print(d)
f = ''.join(d)
print(f)
d = f.split('.')
print(d)
f = ''.join(d)
print(f)
d = f.split('d')
print(d)
f = ''.join(d)
print(f)
d = f.split('e')
print(d)
f = ''.join(d)
print(f)
d = f.split('f')
print(d)
f = ''.join(d)
print(f)
d = f.split('j')
print(d)
f = ''.join(d)
print(f)

