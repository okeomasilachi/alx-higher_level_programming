#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ctn = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ctn += 1
        except IndexError:
            print("Traceback (most recent call last):")
            break
    return ctn
