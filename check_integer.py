# delwin

s=input('enter a integer')
try:
    i=int(s)
    print('valid integer entered',i)
except ValueError as err:
    print(err)

