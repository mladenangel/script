#!/usr/bin/env python3
# delwin

from string import Template

s = Template('$x , glorious $x')
print (s.substitute(x='delwin'))

s = Template("Its´s ${x}tastic!")
print (s.substitute(x='fan'))

s = Template("Make $$ selling $x!")
print(s.substitute(x='slum'))

s = Template('A $thing must never $action.')
d = {}
d['thing']='gentleman'
d['action']='show his socks'
print(d)
print(s.substitute(d))

s = Template('Delwin $the $is best!')
d = {}
d['the']='is'
d['is']='the'
print(d)
print(s.substitute(d))

