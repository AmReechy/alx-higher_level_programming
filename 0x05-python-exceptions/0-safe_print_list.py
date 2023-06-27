#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cmpte = 0
    for index in range(x):
        try:
            print(my_list[index], end='')
            cmpte += 1
        except Exception as error:
            break
    print('')
    return cmpte
