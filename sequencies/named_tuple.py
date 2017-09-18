# delwin


import collections
Circle=collections.namedtuple('Circle','x y radius')
circle=Circle(13,84,9)
print(circle)
circle=circle._replace(radius=12)
print(circle)
circle=circle._replace(x=0,y=10,radius=100)
print(circle)
Dogs=collections.namedtuple('Dogs','rasa color price')
dog=Dogs('Doberman','Black',500)
print(dog)
dog=dog._replace(rasa='PitBull',color='Brown',price=1000)
print(dog)
dog=dict(rasa='Doberman',color='Black',price=1000)
print(dog)

