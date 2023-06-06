#!/usr/bin/python3
def uppercase(str):
    for ric in str:
        ric = ord(ric)
        if ric >= 97 and ric <= 122:
            ric -= 32
        ric = chr(ric)
        print("{}".format(ric), end='')
    print("")
