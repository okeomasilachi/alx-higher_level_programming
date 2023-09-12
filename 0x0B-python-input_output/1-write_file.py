#!/usr/bin/python3

""" holds the write_file function"""


def write_file(filename="", text=""):
    """
    writes the given text to a file with the specified filename.

    Args:
      filename: represents the name of the file you want to
    write to.

    Returns:
      the number of characters written to the file.
    """
    if filename == "":
        return
    else:
        with open(filename, 'w', encoding="utf-8") as file:
            if text != "":
                return file.write(text)
        file.close()
