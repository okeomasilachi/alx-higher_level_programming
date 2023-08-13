#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for val in my_list:
        if type(val) is int or type(val) is float:
            print("{:d}".format(val))
