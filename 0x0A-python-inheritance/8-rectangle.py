#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        try:
            BaseGeometry.integer_validator(self, "height", height)
        except TypeError as e:
            TypeError(e)
        except ValueError as ve:
            ValueError(ve)
        else:
            self.__height = height

        try:
            BaseGeometry.integer_validator(self, "width", width)
        except TypeError as e:
            TypeError(e)
        except ValueError as ve:
            ValueError(ve)
        else:
            self.__width = width
 
            