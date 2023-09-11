#!/usr/bin/python3

"""
Module that host the class MyList(list).
"""


class MyList(list):
    """
    The class MyList is a subclass of the built-in list class in Python
    """
    def print_sorted(self):
        """
        The function `print_sorted` takes a list
        creates a copy of it, sorts the copy in ascending
        order, and then prints the sorted copy.
        """
        self.sort()
        print(self)
