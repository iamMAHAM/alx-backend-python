#!/usr/bin/env python3
"""
sum list : a module
"""


def sum_list(input_list: list[float]) -> float:
    """
    sum a list of float
    """
    sum: float = 0
    i = 0
    for i in range(len(input_list)):
        sum += input_list[i]

    return sum
