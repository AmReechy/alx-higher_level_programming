#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    max_int = 0
    for num in my_list:
        if num > max_int:
            max_int = num
    return (max_int)
