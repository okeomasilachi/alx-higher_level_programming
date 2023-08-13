#!/usr/bin/python3

# prints all integers of a list
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if isinstance(my_list[i], int):
            print("{}".format(my_list[i]))
