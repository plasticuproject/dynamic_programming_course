"""how_sum_tabulation.py"""
from typing import List, Optional, Any
"""
PROBLEM:

Write a function 'how_sum(target_sum, numbers)' that takes in a
target_sum and an array of numbers as arguments.

The function should return an array containing any combination of
elements that add up to exactly the target_sum. If there is no
combination that adds up to the target_sum, then return null.

If there are multiple combinations possible, you may return any
single one.
"""

# Recursive method for reference
'''
def how_sum_recursive(target_sum: int,
                      numbers: List[int]) -> Optional[List[int]]:
    """Recursive method for solving problem using no caching
    or memoization."""
    if target_sum < 0:
        return None
    if target_sum in numbers:
        return [target_sum]
    for num in numbers:
        new_target_sum: int = target_sum - num
        adders: Optional[List[int]] = how_sum_recursive(
            new_target_sum, numbers)
        if adders is not None:
            adders.append(num)
            return adders
    return None
'''


def how_sum(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """Iterative method for solving problem using
    tabulation."""
    table: List[Any] = [None] * (target_sum + 1)
    table[0] = []
    if target_sum in numbers:
        return [target_sum]
    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                advance: int = i + num
                if advance <= target_sum:
                    table[advance] = table[i].copy()
                    table[advance].append(num)
    target_sum_list: Optional[List[int]] = table[target_sum]
    return target_sum_list


# TESTS
assert how_sum(7, [2, 3]) == [3, 2, 2]
assert how_sum(7, [5, 3, 4]) == [4, 3]
assert how_sum(7, [5, 3, 4, 7]) == [7]
assert how_sum(7, [2, 4]) is None
assert how_sum(8, [2, 3, 5]) == [2, 2, 2, 2]
assert how_sum(300, [7, 14]) is None
