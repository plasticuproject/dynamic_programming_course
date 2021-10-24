"""all_construct_tabulation.py"""
from typing import List, Any
"""
PROBLEM:

Write a function 'all_construct(target, word_bank)' that accepts a
target string and an array of strings.

The function should return a 2D array containing all of the ways
that the 'target' can be constructed by concatenating elements of
the 'word_bank' array. Each element of the 2D array should represent
one combination that constructs the 'target'.

You may reuse elements of 'word_bank' as many times as needed.
"""

# Recursive method for reference
'''
def all_construct(target: str, word_bank: List[str]) -> List[List[str]]:
    """Recursive method for solving problem using no caching
    or memoization."""
    construct_list: List[List[str]] = list()
    if target == "":
        return [[]]
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            construct: List[List[str]] = all_construct(new_word, word_bank)
            constructs: List[List[str]] = [[word] + i for i in construct]
            construct_list += constructs
    return construct_list
'''


def all_construct(target: str, word_bank: List[str]) -> List[List[str]]:
    """Iterative method for solving problem using
    tabulation."""
    table: List[List[Any]] = [[]] * (len(target) + 1)
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            advance: int = i + len(word)
            if target[i:].startswith(word):
                construct: List[List[str]] = [_ + [word] for _ in table[i]]
                table[advance] = table[advance] + [_ for _ in construct]
    return table[len(target)]


# TESTS
assert all_construct("purple", [
    "purp",
    "p",
    "ur",
    "le",
    "purpl",
]) == [
    ["purp", "le"],
    ["p", "ur", "p", "le"],
]

assert all_construct("abcdef", [
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
    "ef",
    "c",
]) == [
    ["abc", "def"],
    ["ab", "c", "def"],
    ["abcd", "ef"],
    ["ab", "cd", "ef"],
]

assert all_construct("skateboard", [
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
]) == []

assert all_construct("eeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
]) == []
