#!/usr/bin/python3
"""Defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
