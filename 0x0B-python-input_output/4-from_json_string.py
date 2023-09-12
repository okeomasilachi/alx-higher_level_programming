#!/usr/bin/python3

"""holds the functon that converts json to py obj"""


import json


def from_json_string(my_str):
    """
    converts a JSON string into a Python object.

    Args:
      my_str: string that represents a JSON object.

    Returns:
      the result of parsing the input string as a JSON object.
    """
    return json.loads(my_str)
