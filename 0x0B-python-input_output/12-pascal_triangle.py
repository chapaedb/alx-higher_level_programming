#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing the Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        current_row = triangles[-1]
        new_row = [1]
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(1)
        triangles.append(new_row)
    return triangles
