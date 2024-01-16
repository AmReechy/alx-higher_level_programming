#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

'''
    unit test cases for functions in the module base
'''


class test_base(unittest.TestCase):
    '''
        Testing base
    '''
    def test_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_0(self):
        '''
            Sending an id 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_50(self):
        '''
            Sending a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_negative_id(self):
        '''
            Sending a negative id
        '''
        b = Base(-10)
        self.assertEqual(-10, b.id)

    def test_to_json(self):
        '''
            Testing the json string
        '''
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_id_str(self):
        '''
            Sending an id that is not an int
        '''
        b = Base("reechy")
        self.assertEqual("reechy", b.id)

    def test_to_json_val(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 69)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 69, "y": 0, "size": 1, "x": 0}])


    def test_to_json_Empty(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

