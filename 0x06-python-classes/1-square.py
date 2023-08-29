#!/usr/bin/python3
""" defines a square by: (based on 0-square.py) """


class Square:
    """A class to represent a square."""
    def __init__(self, size):
        """Initialize the square with the given side length.

        The size is the length of one side of the square.
        """
        self.__size = size  # The size of the square is private.
