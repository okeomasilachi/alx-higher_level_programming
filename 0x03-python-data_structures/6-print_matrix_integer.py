#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 0
        for j in i:
            print("{}".format(j), end=" " if k != (len(i) - 1) else "")
            k += 1
        print()
