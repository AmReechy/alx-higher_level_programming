#!/usr/bin/python3
for ric in range(0, 100):
    if ric != 99:
        print("{0:0=2d}, ".format(ric), end='')
    else:
        print('99')
