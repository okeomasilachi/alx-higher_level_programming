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
        def to_json(self):
            that retrieves a dictionary representation of a Student instance
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

    def to_json(self):
        """
        returns the instance variables of an object as a JSON string.

        Returns:
          Dictionary representation of the object's attributes.
        """
        return vars(self)
