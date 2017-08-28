print('if - else')
a = input('a?')
b = input('b?')
print('a =' + str(a))

print(' b =' + str(b))



if (a>10) or (b>10):
    print('(a > 10) or (b > 10)')
elif (a!=5) and (b<=7):
    print('(a != 5) and (b <= 7)')
else:
    print('else')

# nested if
print('neted if')

if (a == 0) or (b > 20):
    if b < 50:
        print('nested-if')
    else:
        print('else-nested-if')
else:
    print('if-else')



