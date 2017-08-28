import time

print('get current time')
now = time.time()
print(now)
print('display readable current time')
print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(now)))
print(time.timezone)


