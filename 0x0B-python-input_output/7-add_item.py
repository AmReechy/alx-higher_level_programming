#!/usr/bin/python3
"""
This is a script that adds all command line arguments
to a Python list, and then save them to a file.
"""

from sys import argv
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"
argc = len(argv)

file_list = []

if exists(file_name):
    file_list = load_from_json_file(file_name)

if (argc == 1):
    save_to_json_file(file_list, file_name)
else:
    for index in range(1, argc):
        file_list.append(argv[index])
    save_to_json_file(file_list, file_name)
