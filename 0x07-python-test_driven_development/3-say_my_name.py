#!/usr/bin/python3
""""
This module contains a function, say_my_name, that prints a name
"""


def say_my_name(first_name, last_name=""):
    '''This function prints name ({first name} {last name})

    Args:
        first_name (str): The fisrt name to be printed
        last_name (str): The last name to be printed

    Raises:
        TypeError: If either the first_name and last_name is not a string

    '''

    name_list = [('first_name', first_name), ('last_name', last_name)]
    for name in name_list:
        if not isinstance(name[1], str):
            raise TypeError(f"{name[0]} must be a string")

    print(f"My name is {first_name} {last_name}")
