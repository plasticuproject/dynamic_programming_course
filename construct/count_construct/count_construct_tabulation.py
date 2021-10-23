"""count_construct_tabulation.py"""
from typing import List
"""
PROBLEM:

Write a function 'count_construct(target, word_bank)' that accepts a
target string and an array of strings.

The function should return the number of ways that the 'target' can
be constructed by concatenating elements of the 'work_bank' array.

You may reuse elements of 'word_bank' as many times as needed.
"""

# Recursive method for reference
'''
def count_construct(target: str, word_bank: List[str]) -> int:
    """Recursive method for solving problem using no caching
    or memoization."""
    count: int = 0
    if target == "":
        return 1
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            count += count_construct(new_word, word_bank)
    return count
'''


def count_construct(target: str, word_bank: List[str]) -> int:
    """Iterative method for solving problem using
    tabulation."""
    table: List[int] = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(target)):
        if table[i] != 0:
            for word in word_bank:
                if target[i:].startswith(word):
                    table[i + len(word)] += table[i]
    return table[len(target)]


# TESTS
assert count_construct("abcdef", [
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
]) == 1

assert count_construct("purple", [
    "purp",
    "p",
    "ur",
    "le",
    "purpl",
]) == 2

assert count_construct("skateboard", [
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
]) == 0

assert count_construct("enterpotentpot", [
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
]) == 4

assert count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
]) == 0
