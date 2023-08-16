#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret = {}
    if not a_dictionary:
        return ret
    for k, i in a_dictionary.items():
        ret[k] = (i * 2)
    return ret
