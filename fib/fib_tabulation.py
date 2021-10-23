"""fib_tabulation.py"""
from typing import List
"""
PROBLEM:

Write a function 'fib(n)' that takes in a number as an agurment.
The function should return the n-th number of the Fibonacci sequence.

The 0th number of the sequence is 0.
The 1st number of the sequence is 1.

To generate the next number of the sequence, we sum the previous two.
"""


def fib(_n: int) -> int:
    """Iterative method for calculating
    nth Fibonacci number using tabulation."""
    if _n == 0:
        return 0
    table: List[int] = [0] * (_n + 1)
    table[1] = 1
    for i in range(2, _n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[_n]


# TESTS
assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(6) == 8
assert fib(7) == 13
assert fib(8) == 21
assert fib(50) == 12586269025
