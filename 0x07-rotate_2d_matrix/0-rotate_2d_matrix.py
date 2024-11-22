#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix (list of lists): The 2D matrix to be rotated.

    Returns:
    - None: The matrix is modified in-place.

    Example:
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> rotate_2d_matrix(matrix)
    >>> print(matrix)
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
