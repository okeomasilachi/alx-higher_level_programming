#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ctn = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ctn += 1
        except IndexError as er:
            print(er, end="")
        else:
            continue
        finally:
            continue
    print()
    return ctn
