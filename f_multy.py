# delwin

def multy(factor):
    def multyx(number):
        return number*factor
    return multyx

x = input('x ')
y = input('y ')
d = multy(x)
print(d(y))


