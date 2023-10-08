#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(3):
        for col in range(3):
            print("{:d}".format(matrix[row][col]), end=" ")

        print()
