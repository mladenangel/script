print('<--Dictonary-->')
print('declare: a={},b={1:"Sea",2:"River",8:"Mountain"}, c={1:{1:"name",2:"email",3:"address"},2:"description"}')
a={}
b={1:'Sea',2:'River',8:'Mountain'}
c={1:{1:'name',2:'email',3:'address'},2:'description'}
d = dict(name='elena',age=30,roles=('manager','consultant'))

print('a,b,c,d')
print(a,b,c,d)
print('key values')
print(b.keys())
print(b.values())
print(b.items())
print('add item')
a.setdefault(2,'car')
a.setdefault(3,'train')
a.setdefault(4,'plain')
print(a)
print('check key')
print('3 in b')
print(3 in b)
print('5 in b')
print(5 in b)
for i in c:
    print i
print(c.values())



 

