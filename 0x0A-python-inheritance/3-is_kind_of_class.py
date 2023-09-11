#!/usr/bin/python3

"""Model that holds the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    The function checks if an object is an instance of a given class.

    Args:
      obj: The object that you want to check the class of.
      a_class: The class to check if the `obj` belongs to or is
    a subclass of.

    Returns:
      boolean value indicating the given object is an instance of a class.
    """
    return isinstance(obj, a_class)
