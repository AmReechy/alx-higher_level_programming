#!/usr/bin/python3
"""This is module to create a base class for several other
classes. The other classes will inherit from the base class"""


import json
import os


class Base:
    """This is a base class to be inherited from"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the rep of list_dictionaries in JSON string format"""
        
        if list_dictionaries is None or  (not list_dictionaries and 
                                          type(list_dictionaries) == list):
            return "[]"
        item_types_bool = [(type(item) == dict) for item in list_dictionaries]
        if (type(list_dictionaries) != list or not all(item_types_bool)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to file"""
        
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None or not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns python list from JSON string representations"""
        
        json_string_list = []

        if json_string is not None and not json_string:
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set
        and returns instance"""
        
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of object instances created"""
        file_name = f"{cls.__name__}.json"
        list_of_instances, list_dictionaries = [], []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances += [cls.create(**dictionary)]
        return list_of_instances

