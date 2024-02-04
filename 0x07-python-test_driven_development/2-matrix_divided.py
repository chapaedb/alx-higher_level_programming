#!/usr/python3

def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix):
        raise TyepeError("matrix must be a matrix (list of lists) of integers/floats"
                for row in matrix:
                    if not all(isinstance(element, (int , float)) for element in row):
                     raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                for row in matrix:
                    if not all(isinstance(elemnt, (int, float)) for element in row):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
