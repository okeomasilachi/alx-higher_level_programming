#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for ci, v in enumerate(r):
            if ci != 0:
                print(" ", end="")
            print("{:d}".format(v), end="")
        print()
