#!/usr/bin/python3

"""
Module that host the functionfor looking up all attributes
and methods of an object.
"""


def lookup(obj):
    """
    "lookup" returns a list of all attributes and methods of an object.

    Args:
      obj: Object to inspect and retrieve its attributes and
    methods.

    Returns:
      A list of all the attributes and methods of the `obj` object.
    """
    return dir(obj)
