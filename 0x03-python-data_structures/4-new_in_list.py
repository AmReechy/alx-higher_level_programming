#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list) - 1
    list_cpy = my_list[:]
    if idx < 0:
        return list_cpy
    elif idx > n:
        return list_cpy
    else:
        list_cpy[idx] = element
        return list_cpy
