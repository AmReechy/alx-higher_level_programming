#!/usr/bin/python3
"""Module with function that insert new line
at the end of line containing specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Insert line of text after each line in the filename
    that contains specific string"""
    
    with open(filename, "r") as f:
        lines_list = file.readlines()
        for i, line in enumerate(lines_list):
            if search_string in line:
                lines_list.insert(i + 1, new_string + "\n")
    with open(filename, "w") as f2:
        for item in lines_list:
            f2.write(item)
