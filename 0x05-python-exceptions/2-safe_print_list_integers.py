#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ctn = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print(my_list[i], end="")
                ctn += 1
    except IndexError as er:
        print(er, end="\n")
        return ctn
    else:
        print()
        return ctn
    finally:
        return ctn
