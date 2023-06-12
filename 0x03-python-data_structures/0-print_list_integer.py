#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for l in my_list:
        if type(l) == int:
            print('{:d}'.format(l))
