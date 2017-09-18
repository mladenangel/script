#delwin

x={'username':'admin','pc':['pc1','pc2','ws1']}
y=x.copy()
y['username']='delwin'
y['pc'].remove('ws1')
print (y)
print (x)
people = {'joe':{'phone':'234','addr':'foo 23'},'bet':{'phone':'2345','addr':'foo 234'}}
print(people['joe'],people['bet'])
print('name joe','phone:',people['joe']['phone'],'address:',people['joe']['addr'])
