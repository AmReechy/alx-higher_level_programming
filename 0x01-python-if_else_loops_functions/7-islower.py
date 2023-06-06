#!/usr/bin/python3

def islower(c):
    mycheck = ord(c)
    if mycheck >= 97 and mycheck <= 122:
        return True
    elif mycheck < 97 or mycheck > 122:
        return False
