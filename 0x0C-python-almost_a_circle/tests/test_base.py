#!/usr/bin/python3

"""
Model for the Base class test case
"""


import unittest
from unittest.mock import patch
from io import StringIO
from base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)


    def test_init_without_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_to_json_string_empty(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty(self):
        data = [{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]')

    def test_from_json_string_empty(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty(self):
        data = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        result = Base.from_json_string(data)
        self.assertEqual(result, [{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}])

if __name__ == '__main__':
    unittest.main()
