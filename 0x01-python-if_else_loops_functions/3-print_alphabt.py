#!/usr/bin/python3
for ric in range(97, 123):
    if ric == 101 or ric == 113:
        continue
    print("{:c}".format(ric), end='')
