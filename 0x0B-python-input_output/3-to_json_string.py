#!/usr/bin/python3

""" holds the to_jason_string function """


import json
def to_json_string(my_obj):
    """
    converts a Python object into a JSON string.

    Args:
      my_obj: the object that you want to convert to a JSON string.
      It can be any valid Python object such as a dictionary,
      list, string, number, boolean, or None.

    Returns:
      a JSON string representation of the input object.
    """
    return json.dumps(my_obj)
