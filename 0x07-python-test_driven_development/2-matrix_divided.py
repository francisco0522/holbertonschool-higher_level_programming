#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix
>>> print(matrix_divided([[1, 2, 3], [4, 5, 6]], 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
    """
    matrixCase1 = "matrix must be a matrix (list of lists) of integers/floats"
    matrixCase2 = "Each row of the matrix must have the same size"
    matrixCase3 = "div must be a number"
    matrixCase4 = "division by zero"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(matrixCase3)
    if div == 0:
        raise ZeroDivisionError(matrixCase4)
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(element, int) or isinstance(element, float)
        for element in [n for row in matrix for n in row]))):
            raise TypeError(matrixCase1)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(matrixCase2)
    return ([list(map(lambda x: round(x / div, 2), i)) for i in matrix])
