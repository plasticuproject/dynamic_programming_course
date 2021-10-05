"""can_construct_memoization.py"""
from functools import lru_cache
from typing import List, Tuple, Dict, Optional
"""
PROBLEM:

Write a function 'can_construct(target, word_bank)' that accepts a
target string and an array of strings.

The function should return a boolean indicating whether or not the
'target' can be constructed by concatenating elements of the
'word_bank' array.

You may reuse elements of 'word_bank' as many times as needed.
"""


def can_construct(target: str, word_bank: List[str]) -> bool:
    """Recursive method for solving problem using no caching
    or memoization."""
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            if can_construct(new_word, word_bank):
                return True
    return False


@lru_cache(maxsize=None)
def can_construct_builtin_memo(target: str, word_bank: Tuple[str]) -> bool:
    """Recursive method for solving problem using python's
    built-in function caching for memoization. Had to change
    second argument from list to tuple type for hashing."""
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            if can_construct_builtin_memo(new_word, word_bank):
                return True
    return False


def can_construct_custom_memo(target: str,
                              word_bank: List[str],
                              memo: Optional[Dict[str, bool]] = None) -> bool:
    """Recursive method for solving problem using custom
    function caching for memoization."""
    if memo is None:
        memo: Dict[str, bool] = dict()
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            if can_construct_custom_memo(new_word, word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


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

TEST_4 = can_construct_builtin_memo("abcdef", (
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
))
assert TEST_4 is True

TEST_5 = can_construct_builtin_memo("skateboard", (
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
))
assert TEST_5 is False

TEST_6 = can_construct_builtin_memo("enterpotentpot", (
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
))
assert TEST_6 is True

TEST_7 = can_construct_builtin_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", (
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
))
assert TEST_7 is False

TEST_8 = can_construct_custom_memo("abcdef", [
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
])
assert TEST_8 is True

TEST_9 = can_construct_custom_memo("skateboard", [
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
])
assert TEST_9 is False

TEST_10 = can_construct_custom_memo("enterpotentpot", [
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
])
assert TEST_10 is True

TEST_11 = can_construct_custom_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
])
assert TEST_11 is False
