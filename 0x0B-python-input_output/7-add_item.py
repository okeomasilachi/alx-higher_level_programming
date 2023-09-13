#!/usr/bin/python3

"""
Script that adds all arguments to a Python list.
and then save them to a file named add_item.json.
If the file doesn’t exist, it should be created
"""


import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


args = sys.argv[1:]
try:
    var = load_from_json_file("add_item.json")
except Exception:
    var = []
finally:
    for item in args:
        var.append(item)

    save_to_json_file(var, "add_item.json")
