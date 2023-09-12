#!/usr/bin/python3

""" holds the function read file """


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
    if filename == "":
        return
    else:
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                print(line, end='')
        file.close()
