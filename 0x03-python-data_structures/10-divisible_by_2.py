#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            ret.append(True)
        else:
            ret.append(False)
    return ret
