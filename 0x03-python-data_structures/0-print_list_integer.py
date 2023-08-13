#!/usr/bin/python3

# prints all integers of a list
def print_list_integer(my_list=[]):
    i = 0
    while i != (len(my_list) - 1):
        if isinstance(my_list[i], int):
            print("{}".format(my_list[i]))
        i += 1
