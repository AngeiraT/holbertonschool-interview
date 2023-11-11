#!/usr/bin/python3
"""Module pascal_triangle."""


def pascal_triangle(n):
    """
    Represent the Pascal's triangle of n.

    Args:
        n (int): integer to represent
    Returns:
        list of lists of integers
    """
    if n <= 0:
        return []
    pascal = [[1]]
    while len(pascal) != n:
        previous = pascal[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        pascal.append(current)
    return pascal
