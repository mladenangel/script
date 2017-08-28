print('Tuples')

print('declate tuples: a=(), b=(3,2,7), c=("Fort","BMW","Toyota"),d=(3,(5,"London"),12)')
a=()
b=(3,5,7)
c=('Ford','BMW','Toyota')
d=(3,(5,'London'),12)
print('tuples:')
print(a,b,c,d)

print('get length a b c d')
print(len(a),len(b),len(c),len(d))
print('get item b[2]')
print(b[2])
print('print tuple d')
for cat in d:
    print(cat)
print('get index b.index(7)')
print(b.index(7))
print('get index c.index("Toyota")')
print(c.index('Toyota'))
print('print tuple c')
for car in c:
    print(car)



