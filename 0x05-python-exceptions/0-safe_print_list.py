#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    ct = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            ct += 1
        except IndexError as er:
            continue
    print()
    return ct
