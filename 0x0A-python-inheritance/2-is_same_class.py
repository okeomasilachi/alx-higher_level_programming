#!/usr/bin/python3

"""Model that holds the function is_same_class"""


def is_same_class(obj, a_class):
    """
    The function checks if an object is an instance of a specific class.

    Args:
      obj: object to check the class of.
      a_class: The class that we want to check if the `obj` belongs to.

    Returns:
      True if the type of the object obj is the same as the class
    a_class. Otherwise, it returns False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
