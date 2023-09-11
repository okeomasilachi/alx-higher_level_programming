#!/usr/bin/python3

"""Model that holds the function is_kind_of_class"""


def inherits_from(obj, a_class):
    """
    Checks if an object inherits from a specific class.

    Args:
      obj: Object that you want to check if it inherits from a specific
    class.
      a_class: Class that we want to check if `obj` inherits from.

    Returns:
      `True` if the object `obj` is an instance of a class that
    inherits from the class `a_class`, and `False` otherwise.
    """
    tp = type(obj)
    return issubclass(tp, a_class)
