#!/usr/bin/python3

""" modul that holds the function read file """


def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
      filename: Represents the name of the file that you want
    to read.

    Returns:
      empty string if no parameter, the function will return
    `None`. Otherwise, print the contents of the file and not return anything.
    """
    if not filename:
        return
    with open(filename, 'r', encoding='utf8') as file:
        print(file.read())
