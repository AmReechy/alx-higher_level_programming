#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary.keys():
        temp = {key: (a_dictionary[key] * 2)}
        new_dict.update(temp)
