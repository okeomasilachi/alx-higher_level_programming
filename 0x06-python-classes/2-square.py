#!/usr/bin/python3

""" defines a square by: (based on 1-square.py) """


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int, optional): The size of the square's sides. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # The size of the square is private.
