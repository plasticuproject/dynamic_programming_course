"""grid_traveler_memoization.py"""
from functools import lru_cache
from typing import Optional, Dict, Tuple
"""
PROBLEM:

Say that you are a traveler on a 2D grid. You begin in the
top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right.

In how many ways can you travel to the goal in a grid
with dimenstions m * n?

Write a function 'grid_traveler(m, n)' that calculates this.
"""


@lru_cache(maxsize=None)
def grid_traveler_builtin_memo(_m: int, _n: int) -> int:
    """Recursive method for solving problem using python's
    built-in function caching for memoization."""
    if _m == 1 and _n == 1:
        return 1
    if _m == 0 or _n == 0:
        return 0
    return (grid_traveler_builtin_memo(_m - 1, _n) +
            grid_traveler_builtin_memo(_m, _n - 1))


def grid_traveler_custom_memo(
        _m: int,
        _n: int,
        memo: Optional[Dict[Tuple[int, int], int]] = None) -> int:
    """Recursive method for solving problem using custom
    function caching for memoization."""
    position: Tuple[int, int] = (_m, _n)
    trans_postion: Tuple[int, int] = (_n, _m)
    if memo is None:
        memo = dict()
    if position in memo:
        return memo[position]
    if trans_postion in memo:
        return memo[trans_postion]
    if _m == 1 and _n == 1:
        memo[position] = 1
        return 1
    if _m == 0 or _n == 0:
        memo[position] = 0
        return 0
    memo[position] = (grid_traveler_custom_memo(_m - 1, _n, memo) +
                      grid_traveler_custom_memo(_m, _n - 1, memo))
    return memo[position]


# TESTS
assert grid_traveler_builtin_memo(1, 1) == 1
assert grid_traveler_builtin_memo(2, 3) == 3
assert grid_traveler_builtin_memo(3, 2) == 3
assert grid_traveler_builtin_memo(3, 3) == 6
assert grid_traveler_builtin_memo(18, 18) == 2333606220

assert grid_traveler_custom_memo(1, 1) == 1
assert grid_traveler_custom_memo(2, 3) == 3
assert grid_traveler_custom_memo(3, 2) == 3
assert grid_traveler_custom_memo(3, 3) == 6
assert grid_traveler_custom_memo(18, 18) == 2333606220
