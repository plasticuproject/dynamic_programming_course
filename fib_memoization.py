"""fib_memoization.py"""
from functools import lru_cache
from typing import Optional


# Iterative method
def fib(_n: int) -> int:
    """Iterative method for calculating
    nth fibonacci number."""
    if _n <= 2:
        return 1
    _a, _b, _c = 1, 1, 0
    for i in range(_n - 2):  # pylint: disable=unused-variable
        _c = _a + _b
        _a = _b
        _b = _c
    return _c


# Recursive using built-in memoization
@lru_cache(maxsize=None)
def fib_recur_builtin_memo(_n: int) -> int:
    """Recursive method for calculating nth fibonacci
    number using pythons built in function cacheing
    for memoization."""
    if _n <= 2:
        return 1
    return fib_recur_builtin_memo(_n - 1) + fib_recur_builtin_memo(_n - 2)


# Recursive using custom memoization
def fib_recur_custom_memo(_n: int, memo: Optional[dict] = None) -> int:
    """Recursive method for calculating nth fibonacci
    number using custom function cacheing for
    memoization."""
    if memo is None:
        memo = {}
    if _n in memo:
        return memo[_n]
    if _n <= 2:
        return 1
    memo[_n] = fib_recur_custom_memo(
        _n - 1, memo=memo) + fib_recur_custom_memo(_n - 2, memo=memo)
    return memo[_n]


# TESTS
assert fib(50) == 12586269025
assert fib_recur_builtin_memo(50) == 12586269025
assert fib_recur_custom_memo(50) == 12586269025
