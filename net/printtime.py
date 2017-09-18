#!/usr/bin/env python
# delwin


import ntplib
from time import ctime

def print_time():
    ntp=ntplib.NTPClient()
    response=ntp.request('pool.ntp.org')
    print(ctime(response.tx_time))

if __name__=='__main__':
    print_time()


