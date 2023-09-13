#!/usr/bin/python3

"""
holds function that returns the dictionary description,
with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    converts a class object into a JSON-compatible dictionary.

    Args:
      obj: Instance of a class that you want to convert to a JSON
    representation.

    Returns:
      a dictionary representation of the attributes and values
      of the input object.
    """
    return vars(obj)
