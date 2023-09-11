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

    def integer_validator(self, name, value):
        """
        Checks if a given value is an integer and if it is greater than
        0.

        Args:
          name: string that represents the name of the
           variable being validated.
          value: value that needs to be validated as an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
