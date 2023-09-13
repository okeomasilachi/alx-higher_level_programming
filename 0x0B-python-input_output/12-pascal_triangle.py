#!/usr/bin/python3

"""
This model holds the funtion that
return a list of lists that represents
the pascal triangle
"""


def pascal_triangle(n):
    """
    Generate the first n rows of Pascal's triangle.

    Args:
        n: The number of rows to generate.

    Returns:
        A list of lists, where each inner list is a row of the triangle.
    """
    ok = []
    if n <= 0:
        return ok
    tri = [[1]]
    for i in range(1, n):
        rw = [1]
        for j in range(1, i):
            rw.append(tri[i - 1][j - 1] + tri[i - 1][j])
        rw.append(1)
        tri.append(rw)
    return tri
