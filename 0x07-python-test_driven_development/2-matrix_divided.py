#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the divided elements.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if the div is not a number (integer or float).
        ZeroDivisionError: If the div is equal to 0.
        TypeError: If each row of the matrix does not have the same size.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    divided_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return divided_matrix
