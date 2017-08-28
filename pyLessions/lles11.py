print('Lists')

print('----declare lists')
numbers = []
a = [2,7,10,8]
cities =['Berlin','Barcelona','Madrid','Malaga']
b = [10 , 3 ,'Aplle',8,'Python','Strawberry']
c = range(1,10,2)

print('-----print (lists)')
print(a)
for city in cities:
    print(city)
print(b)
print(c)

print('-----get length of lists')
print(len(a))
print(len(cities))

print('---add item')
numbers.append(19)
numbers.append(5)
cities.append('London')
for i in numbers:
    print(i)
for city in cities:
    print(city)

print('----get item')
print(cities[2])
print(a[3])

print('----sorting')
print(a.sort())

print('---edit item')
cities[2] = 'new city'
for city in cities:
    print(city)

print('---remove item')
a.remove(8)
del cities[2]
for city in cities:
    print(city)


