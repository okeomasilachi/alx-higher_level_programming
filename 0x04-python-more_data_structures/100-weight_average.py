#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    ad = 0
    if not my_list:
        return mul
    for i in my_list:
        mul += (i[0] * i[1])
        ad += i[1]
    return (mul / ad)
