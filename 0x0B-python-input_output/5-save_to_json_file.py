#!/usr/bin/python3

"""holds the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """
    The function saves a Python object to a JSON file.

    Args:
      my_obj: The object that you want to save to the JSON file. It can be any
    valid JSON serializable object, such as a dictionary, list, or string.
      filename: string that represents the name of the file where the JSON
    data will be saved.

    Returns:
      nothing if the filename is empty or if the my_obj is empty. Otherwise,
      it writes the JSON representation of my_obj to the specified file.
    """
    if not filename:
        return
    else:
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json.dumps(my_obj))
