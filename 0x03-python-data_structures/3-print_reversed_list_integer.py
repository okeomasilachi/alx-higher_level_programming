#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = (len(my_list) - 1)
    t = int, float
    while i > -1:
        if isinstance(my_list[i], t):
            print("{}".format(my_list[i]))
        i -= 1
