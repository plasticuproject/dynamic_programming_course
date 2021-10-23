"""best_sum_tabulation.py"""
from typing import List, Optional, Any
"""
PROBLEM:

Write a function 'best_sum(target_sum, numbers)' that takes in a
target_sum and an array of numbers as arguments.

The function should return an array containing the shortest
combination of numbers that add up to exactly the target_sum.

If there is a tie for the shortest combination, you may return any
one of the shortest.
"""

# Recursive method for reference
'''
def best_sum_recursive(target_sum: int,
                       numbers: List[int]) -> Optional[List[int]]:
    """Recursive method for solving problem using no caching
    or memoization."""
    if target_sum < 0:
        return None
    if target_sum in numbers or target_sum == 0:
        return [target_sum]
    shortest_combo: Optional[List[int]] = None
    for num in numbers:
        new_target_sum: int = target_sum - num
        adders: Optional[List[int]] = best_sum_recursive(
            new_target_sum, numbers)
        if adders is not None:
            combo: List[int] = adders.copy()
            combo.insert(0, num)
            if shortest_combo is None or len(combo) < len(shortest_combo):
                shortest_combo = combo
    return shortest_combo
'''


def best_sum(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """Iterative method for solving problem using
    tabulation."""
    table: List[Any] = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                advance: int = i + num
                if advance <= target_sum:
                    if not table[advance] or len(table[i]) + 1 < len(
                            table[advance]):
                        table[advance] = table[i].copy()
                        table[advance].append(num)
    target_sum_list: Optional[List[int]] = table[target_sum]
    return target_sum_list


# TESTS
assert best_sum(7, [5, 3, 4, 7]) == [7]
assert best_sum(7, [5, 3, 4]) == [3, 4]
assert best_sum(8, [2, 3, 5]) == [3, 5]
assert best_sum(8, [1, 4, 5]) == [4, 4]
assert best_sum(100, [1, 2, 5, 25]) == [25, 25, 25, 25]
