#!/usr/bin/python3

"""model for the geometry base class"""


class BaseGeometry:
    """
    The BaseGeometry class is a base class for geometry-related classes.
    """
    def area(self):
        """
        The function area() raises an exception
         indicating that it is not implemented.
        """
        raise Exception("area() is not implemented")
