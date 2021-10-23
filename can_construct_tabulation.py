"""can_construct_tabulation.py"""
from typing import List
"""
PROBLEM:

Write a function 'can_construct(target, word_bank)' that accepts a
target string and an array of strings.

The function should return a boolean indicating whether or not the
'target' can be constructed by concatenating elements of the
'word_bank' array.

You may reuse elements of 'word_bank' as many times as needed.
"""

# Recursive method for reference
'''
def can_construct_recursive(target: str, word_bank: List[str]) -> bool:
    """Recursive method for solving problem using no caching
    or memoization."""
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            if can_construct_recursive(new_word, word_bank):
                return True
    return False
'''


def can_construct(target: str, word_bank: List[str]) -> bool:
    """Iterative method for solving problem using
    tabulation."""
    table: List[bool] = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i:].startswith(word):
                    table[i + len(word)] = True
    return table[len(target)]


# TESTS
TEST_1 = can_construct("abcdef", [
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
])
assert TEST_1 is True

TEST_2 = can_construct("skateboard", [
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
])
assert TEST_2 is False

TEST_3 = can_construct("enterpotentpot", [
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
])
assert TEST_3 is True
