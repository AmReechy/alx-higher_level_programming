#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    templist = []
    for i,num in enumerate(my_list):
        if i == idx:
            continue
        templist.append(num)
    mylist = templist
    return mylist
