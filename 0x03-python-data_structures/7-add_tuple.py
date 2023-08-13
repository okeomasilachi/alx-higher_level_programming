#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    app_t = (0, )
    ret_1, ret_2 = tuple_a, tuple_b
    len_a, len_b = len(tuple_a), len(tuple_b)
    while len_a < 2:
        tuple_a += app_t
        len_a = len(tuple_a)
    while len_b < 2:
        tuple_b += app_t
        len_b = len(tuple_b)
    ret = tuple_a[0] + tuple_b[0], \
        tuple_a[1] + tuple_b[1]
    tuple_a, tuple_b = ret_1, ret_2
    del ret_1, ret_2, app_t
    return ret
