#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError(f"width must be an integer")
        elif width < 1:
            raise ValueError(f"width must be greater than 0")
        elif not isinstance(height, int):
            raise TypeError(f"height must be an integer")
        elif height < 1:
            raise ValueError(f"height must be greater than 0")
        else:
            self.__height = height
            self.__width = width
        
