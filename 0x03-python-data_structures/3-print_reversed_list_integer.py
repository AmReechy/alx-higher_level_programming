#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0 or not my_list:
        return None
    my_list = [my_list[i] for i in range(-1 * len(my_list), 0)]
    for num in my_list[-1:0:-1]:
        print('{:d}'.format(num))