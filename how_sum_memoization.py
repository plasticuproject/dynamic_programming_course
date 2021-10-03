"""how_sum_memoization.py"""
from functools import lru_cache
from typing import List, Dict, Union, Optional
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


@lru_cache(maxsize=None)
def how_sum_builtin_memo(target_sum: int,
                         numbers: List[int]) -> Union[List[int], None]:
    """Recursive method for solving problem using python's
    built-in function caching for memoization. Had to change
    second argument and return from list to tuple type for hashing."""
    numbers = list(numbers)
    if target_sum < 0:
        return None
    if target_sum in numbers or target_sum == 0:
        return (target_sum, )
    for num in numbers:
        new_target_sum: int = target_sum - num
        adders: Union[List[int],
                      None] = how_sum_builtin_memo(new_target_sum,
                                                   tuple(numbers))
        if adders is not None:
            adders: List[int] = list(adders)
            adders.append(num)
            return tuple(adders)
    return None


def how_sum_custom_memo(
        target_sum: int,
        numbers: List[int],
        memo: Optional[Dict[int, List[int]]] = None) -> Union[List[int], None]:
    """Recursive method for solving problem using custom
    function caching for memoization."""
    if memo is None:
        memo: Dict[int, List[int]] = dict()
    if target_sum < 0:
        return None
    if target_sum in numbers or target_sum == 0:
        return [target_sum]
    if target_sum in memo:
        return memo[target_sum]
    for num in numbers:
        new_target_sum: int = target_sum - num
        adders: Union[List[int],
                      None] = how_sum_custom_memo(new_target_sum, numbers,
                                                  memo)
        if adders is not None:
            adders.append(num)
            memo[new_target_sum]: List[int] = adders
            return adders
    memo[target_sum]: None = None
    return None


# TESTS
assert how_sum_builtin_memo(7, (2, 3)) == (3, 2, 2)
assert how_sum_builtin_memo(7, (5, 3, 4, 7)) == (7, )  # (4, 3)
assert how_sum_builtin_memo(7, (2, 4)) is None
assert how_sum_builtin_memo(8, (2, 3, 5)) == (2, 2, 2, 2)
assert how_sum_builtin_memo(300, (7, 14)) is None

assert how_sum_custom_memo(7, [2, 3]) == [3, 2, 2]
assert how_sum_custom_memo(7, [5, 3, 4, 7]) == [7]  # [4, 3]
assert how_sum_custom_memo(7, [2, 4]) is None
assert how_sum_custom_memo(8, [2, 3, 5]) == [2, 2, 2, 2]
assert how_sum_custom_memo(300, [7, 14]) is None
