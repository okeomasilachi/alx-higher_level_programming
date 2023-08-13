#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = len(my_list) - 1
    lis = my_list
    while i > 1:
        j = 0
        while j < i:
            if lis[j] > lis[j + 1]:
                temp = lis[j]
                lis[j] = lis[j + 1]
                lis[j + 1] = temp
            j += 1
        i -= 1
    return lis[len(my_list) - 1]
