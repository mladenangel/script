#!/usr/bin/env python3
# delwin
import sys
import fileinput
import argparse

def numberline(script):
    for line in fileinput.input(script):
    
        line = line.rstrip()
        num = fileinput.lineno()
        print('%-40s # %2i' %(line,num))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Numberlines a script')
    parser.add_argument('--script', action="store", dest="script", type=str, required=True)
    given_args = parser.parse_args() 
    script  = given_args.script
    numberline(script)

