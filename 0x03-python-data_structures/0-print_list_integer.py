#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for val in my_list:
        if isinstance(val, int):
            print("{}".format(val))
