"""can_sum_tabulation.py"""
from typing import List, Set
"""
PROBLEM:

Write a function 'can_sum(target_sum, numbers)' that takes in a
target_sum and an array of numbers as arguments.

The funciton should return a boolean indicating whether or not it
is possible to generate the target_sum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.
"""

# Recursive method for reference
'''
def can_sum_recursive(target_sum: int, numbers: List[int]) -> bool:
    """Recursive method for solving problem using no caching
    or memoization."""
    number_set: Set[int] = set(numbers)
    if target_sum < 0:
        return False
    if target_sum in number_set or target_sum == 0:
        return True
    if (1 in number_set) or (2 in number_set and target_sum % 2 == 0):
        return True
    for num in number_set:
        new_target_sum: int = target_sum - num
        if can_sum_recursive(new_target_sum, list(number_set)) is True:
            return True
    return False
'''


def can_sum(target_sum: int, numbers: List[int]) -> bool:
    """Interative method for solving problem using
    tabulation."""
    number_set: Set[int] = set(numbers)
    table: List[bool] = [False] * (target_sum + 1)
    table[0] = True
    for i in range(target_sum):
        if table[i] is True:
            for num in number_set:
                if i + num <= target_sum:
                    table[i + num] = True
    return table[target_sum]


# TESTS
assert can_sum(7, [2, 3]) is True
assert can_sum(7, [5, 3, 4, 7]) is True
assert can_sum(7, [2, 4]) is False
assert can_sum(8, [2, 3, 5]) is True
assert can_sum(300, [7, 14]) is False
