#!/usr/bin/python3

# prints all integers of a list
def print_list_integer(my_list=[]):
    for val in my_list:
        if isinstance(val, int):
            print("{}".format(val))
