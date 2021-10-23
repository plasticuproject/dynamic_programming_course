"""best_sum_memoization.py"""
from functools import lru_cache
from typing import List, Tuple, Dict, Optional
"""
PROBLEM:

Write a function 'best_sum(target_sum, numbers)' that takes in a
target_sum and an array of numbers as arguments.

The function should return an array containing the shortest
combination of numbers that add up to exactly the target_sum.

If there is a tie for the shortest combination, you may return any
one of the shortest.
"""


def best_sum(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """Recursive method for solving problem using no caching
    or memoization."""
    if target_sum < 0:
        return None
    if target_sum in numbers or target_sum == 0:
        return [target_sum]
    shortest_combo: Optional[List[int]] = None
    for num in numbers:
        new_target_sum: int = target_sum - num
        adders: Optional[List[int]] = best_sum(new_target_sum, numbers)
        if adders is not None:
            combo: List[int] = adders.copy()
            combo.insert(0, num)
            if shortest_combo is None or len(combo) < len(shortest_combo):
                shortest_combo = combo
    return shortest_combo


@lru_cache(maxsize=None)
def best_sum_builtin_memo(target_sum: int,
                          numbers: Tuple[int]) -> Optional[Tuple[int, ...]]:
    """Recursive method for solving problem using python's
    built-in function caching for memoization. Had to change
    second argument and return from list to tuple type for hashing."""
    numbers_list: List[int] = list(numbers)
    if target_sum < 0:
        return None
    if target_sum in numbers_list or target_sum == 0:
        return (target_sum, )
    shortest_combo: Optional[List[int]] = None
    for num in numbers_list:
        new_target_sum: int = target_sum - num
        adders: Optional[Tuple[int, ...]] = best_sum_builtin_memo(
            new_target_sum, tuple(numbers_list))
        if adders is not None:
            adders_list: List[int] = list(adders)
            combo: List[int] = adders_list.copy()
            combo.insert(0, num)
            if shortest_combo is None or len(combo) < len(shortest_combo):
                shortest_combo = combo
    if shortest_combo is not None:
        return tuple(shortest_combo)
    return None


def best_sum_custom_memo(
    target_sum: int,
    numbers: List[int],
    memo: Optional[Dict[int,
                        Optional[List[int]]]] = None) -> Optional[List[int]]:
    """Recursive method for solving problem using custom
    function caching for memoization."""
    if memo is None:
        memo = dict()
    if target_sum in memo:
        return memo[target_sum]
    if target_sum < 0:
        return None
    if target_sum in numbers or target_sum == 0:
        return [target_sum]
    shortest_combo: Optional[List[int]] = None
    for num in numbers:
        new_target_sum: int = target_sum - num
        adders: Optional[List[int]] = best_sum_custom_memo(
            new_target_sum, numbers, memo)
        if adders is not None:
            combo: List[int] = adders.copy()
            combo.insert(0, num)
            if shortest_combo is None or len(combo) < len(shortest_combo):
                shortest_combo = combo
    memo[target_sum] = shortest_combo
    return shortest_combo


# TESTS
assert best_sum(7, [5, 3, 4, 7]) == [7]
assert best_sum(7, [5, 3, 4]) == [3, 4]
assert best_sum(8, [2, 3, 5]) == [3, 5]
assert best_sum(8, [1, 4, 5]) == [4, 4]

assert best_sum_builtin_memo(7, (5, 3, 4, 7)) == (7, )
assert best_sum_builtin_memo(7, (5, 3, 4)) == (3, 4)
assert best_sum_builtin_memo(8, (2, 3, 5)) == (3, 5)
assert best_sum_builtin_memo(8, (1, 4, 5)) == (4, 4)
assert best_sum_builtin_memo(100, (1, 2, 5, 25)) == (25, 25, 25, 25)

assert best_sum_custom_memo(7, [5, 3, 4, 7]) == [7]
assert best_sum_custom_memo(7, [5, 3, 4]) == [3, 4]
assert best_sum_custom_memo(8, [2, 3, 5]) == [3, 5]
assert best_sum_custom_memo(8, [1, 4, 5]) == [4, 4]
assert best_sum_custom_memo(100, [1, 2, 5, 25]) == [25, 25, 25, 25]
