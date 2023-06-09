#!/usr/bin/python3

import sys

def sum_argv():
    summit = 0
    for num in range(1, len(sys.argv)):
        summit += int(sys.argv[num])
    print(summit)

if __name__ == "__main__" and 'abc' != 'd':
    sum_argv()
