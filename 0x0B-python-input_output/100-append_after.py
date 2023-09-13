#!/usr/bin/python3

"""
holds Write a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    reads a file, searches for a specific string in each line,
    and appends a new string after the line containing the search string.

    Args:
      filename: The name of the file you want to modify.
                It should include thefile extension (e.g., "example.txt").
      search_string: The string that you want to search for in each
                line of the file. If the `search_string` is found in a line,
                the `new_string` will be appended after that line in the file.
      new_string: The string that you want to append after the line that
                contains the `search_string`.
    """
    ret = []
    with open(filename, 'r+', encoding="utf-8") as file:
        for line in file:
            ret.append([line])
            if search_string in line:
                ret.append([new_string])
        file.close

    with open(filename, 'w', encoding="utf-8") as file:
        for i in ret:
            file.write(i[0])
