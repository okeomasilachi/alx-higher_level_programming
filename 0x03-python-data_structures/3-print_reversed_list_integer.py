#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    i = (len(my_list) - 1)
    t = int, float
    while i > -1:
        if type(my_list[i]) is int or type(my_list[i]) is float:
            print("{:d}".format(my_list[i]))
        else:
            message = "Traceback (most recent call last):"
            print(f"{message}")
            return
        i -= 1
