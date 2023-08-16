#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret = []
    if not matrix:
        return ret
    ret += [list(map(lambda x: x ** 2, i)) for i in matrix]
    return ret
