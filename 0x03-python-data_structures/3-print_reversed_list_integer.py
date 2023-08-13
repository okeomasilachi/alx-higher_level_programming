#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = (len(my_list) - 1)
    while i > -1:
        if type(my_list[i]) is int or type(my_list[i]) is float:
            print("{}".format(my_list[i]))
        i -= 1
