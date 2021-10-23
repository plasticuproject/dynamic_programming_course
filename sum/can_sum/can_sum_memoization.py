"""can_sum_memoization.py"""
from functools import lru_cache
from typing import Optional, List, Dict, Set, Tuple
"""
PROBLEM:

Write a function 'can_sum(target_sum, numbers)' that takes in a
target_sum and an array of numbers as arguments.

The funciton should return a boolean indicating whether or not it
is possible to generate the target_sum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.
"""


@lru_cache(maxsize=None)
def can_sum_builtin_memo(target_sum: int, numbers: Tuple[int]) -> bool:
    """Recursive method for solving problem using python's
    built-in function caching for memoization. Had to change
    second argument from list to tuple type for hashing."""
    number_set: Set[int] = set(numbers)
    if target_sum < 0:
        return False
    if target_sum in number_set:
        return True
    if (1 in number_set) or (2 in number_set and target_sum % 2 == 0):
        return True
    for num in number_set:
        new_target_sum: int = target_sum - num
        if can_sum_builtin_memo(new_target_sum, tuple(number_set)) is True:
            return True
    return False


def can_sum_custom_memo(target_sum: int,
                        numbers: List[int],
                        memo: Optional[Dict[int, bool]] = None) -> bool:
    """Recursive method for solving problem using custom
    function caching for memoization."""
    number_set: Set[int] = set(numbers)
    if memo is None:
        memo = dict()
    if target_sum in memo:
        return memo[target_sum]
    if target_sum < 0:
        return False
    if target_sum in number_set:
        return True
    if (1 in number_set) or (2 in number_set and target_sum % 2 == 0):
        return True
    for num in number_set:
        new_target_sum: int = target_sum - num
        if can_sum_custom_memo(new_target_sum, list(number_set), memo) is True:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


# TESTS
assert can_sum_builtin_memo(7, (2, 3)) is True
assert can_sum_builtin_memo(7, (5, 3, 4, 7)) is True
assert can_sum_builtin_memo(7, (2, 4)) is False
assert can_sum_builtin_memo(8, (2, 3, 5)) is True
assert can_sum_builtin_memo(300, (7, 14)) is False

assert can_sum_custom_memo(7, [2, 3]) is True
assert can_sum_custom_memo(7, [5, 3, 4, 7]) is True
assert can_sum_custom_memo(7, [2, 4]) is False
assert can_sum_custom_memo(8, [2, 3, 5]) is True
assert can_sum_custom_memo(300, [7, 14]) is False
