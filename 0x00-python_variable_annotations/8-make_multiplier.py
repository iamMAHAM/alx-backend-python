#!/usr/bin/env python3

"""
8-make: make a multiplier 
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplies a float by multiplier.
    """
    def func(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return func
