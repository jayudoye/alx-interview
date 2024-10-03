#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a pascal triangle of size n"""
    if n <= 0:
        return []
    res = [[1]]
    for i in range(1, n):
        row = [1] * (i + 1)
        prev = res[-1]
        for j in range(1, i):
            row[j] = prev[j] + prev[j - 1]
        res.append(row)

    return res
