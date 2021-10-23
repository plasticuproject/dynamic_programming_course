"""grid_traveler_tabulation.py"""
from typing import List
"""
PROBLEM:

Say that you are a traveler on a 2D grid. You begin in the
top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right.

In how many ways can you travel to the goal in a grid
with dimenstions m * n?

Write a function 'grid_traveler(m, n)' that calculates this.
"""

# Recursive method for reference
'''
def grid_traveler_recursive(_m: int, _n: int) -> int:
    """Recursive method for solving problem using no
    cashing or memoization."""
    if _m == 1 and _n == 1:
        return 1
    if _m == 0 or _n == 0:
        return 0
    return (grid_traveler_recursive(_m - 1, _n) +
            grid_traveler_recursive(_m, _n - 1))
'''


def grid_traveler(_m: int, _n: int) -> int:
    """Iterive method for solving problem using
    tabulation."""
    table: List[List[int]] = [[0] * (_n + 1) for i in range(_m + 1)]
    table[1][1] = 1
    for i in range(_m + 1):
        for j in range(_n + 1):
            current: int = table[i][j]
            if j + 1 <= _n:
                table[i][j + 1] += current
            if i + 1 <= _m:
                table[i + 1][j] += current
    return table[_m][_n]


# TESTS

assert grid_traveler(1, 1) == 1
assert grid_traveler(2, 3) == 3
assert grid_traveler(3, 2) == 3
assert grid_traveler(3, 3) == 6
assert grid_traveler(18, 18) == 2333606220
