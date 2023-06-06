#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > (len(str) - 1):
        return str
    str_cop = ''
    for ind, elem in enumerate(str, 0):
        if ind == n:
            continue
        str_cop += elem
    return str_cop
