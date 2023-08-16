#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k, i in sorted(a_dictionary.items()):
        print("{}: {}".format(k, i))
