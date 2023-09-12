#!/usr/bin/python3

"""holds the load_from_json_file function"""


import json


def load_from_json_file(filename):
    """
    loads data from a JSON file and returns it as a Python object.

    Args:
      filename: String that represents the name of the JSON file that you
    want to load data from.

    Returns:
      the contents of the JSON file as a Python object.
    """
    if not filename:
        return
    else:
        with open(filename, encoding="utf-8") as file:
            return json.loads(file.read())
