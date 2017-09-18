# delwin

import time
import random
from random import randrange
def findMin(alist):
    overallmin=alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin
#print(findMin([5,4,2,1,0]))
#print(findMin([10,1,2,34,56,7]))

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print('size:%d time: %f' %(listSize, end-start))


