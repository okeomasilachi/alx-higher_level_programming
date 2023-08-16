#!/usr/bin/python3
def uniq_add(my_list=[]):
    ret = 0
    if not my_list:
        return ret
    uniq = list(set(my_list))
    for i in range(len(uniq)):
        ret += uniq[i]
    return ret
