#!/usr/bin/python3

"""
holds the class Student that defines a student by:
    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with
        first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
    Public method
        def to_json(self, attrs=None):
            retrieves adictionary representation of a Student instance
            If attrs is a list of strings, only attribute names
            contained in this list must be retrieved.
            Otherwise, all attributes must be retrieved
"""


class Student:
    """
    The Student class is a blueprint for creating objects
    that represent students.
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes the attributes of a class object.

        Args:
          first_name: The first name of the person.
          last_name: store the last name of a person.
          age: store the age of a person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        converts an object's attributes into a JSON-like dictionary, optionally
        filtering the attributes based on a given list.

        Args:
          attrs: list of attributes that you want to include in the JSON
        representation of the object. If `attrs` is `None`,
        all attributes of the object will be included in the JSON.

        Returns:
          JSON representation of the object.
        """
        ret = vars(self)
        emt = {}
        if isinstance(attrs, list):
            for i in attrs:
                for j, k in ret.items():
                    if i == j:
                        emt[j] = k
            return emt
        else:
            return ret

    def reload_from_json(self, json):
        """
        reloads data from a JSON object and
        assigns the values to attributes of an object.

        Args:
          json: dictionary containing key-value pairs.
        """
        for i, v in json.items():
            self.i = v
