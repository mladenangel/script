#!/usr/bin/env python3
# delwin

from math import pi
d = '%s plus %s equals %s'%(1,1,2)
print(d)

d = 'Price of eggs: $%d' %42
print(d)

d = 'Hex price of eggs: %x' %42
print(d)
p = 'Pi:%f...'%pi
print(p)
p = 'Very inexact estimate of pi:%40f'%pi
print(p)

p = ('Using string: %s' % 42)
print(p)

p = 'Using repr:%r' %42
print(p)

d = 23455
p = repr(d)
print(p)
s = str(d)
print(s)

print('%40f' %pi)
print('%30.5f' %pi)
print('%.2f' %pi)
print('%40.5s' %'Guido van Rossum')
print('%40.*s' %(5,'Guido van Rossum'))
 

