"""count_construct_memoization.py"""
from functools import lru_cache
from typing import List, Tuple, Dict, Optional
"""
PROBLEM:

Write a function 'count_construct(target, word_bank)' that accepts a
target string and an array of strings.

The function should return the number of ways that the 'target' can
be constructed by concatenating elements of the 'work_bank' array.

You may reuse elements of 'word_bank' as many times as needed.
"""


def count_construct(target: int, word_bank: List[int]) -> int:
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


@lru_cache(maxsize=None)
def count_construct_builtin_memo(target: int, word_bank: Tuple[int]) -> int:
    """Recursive method for solving problem using python's
    built-in function caching for memoization. Had to change
    second argument from list to tuple type for hashing."""
    count: int = 0
    if target == "":
        return 1
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            count += count_construct_builtin_memo(new_word, word_bank)
    return count


def count_construct_custom_memo(target: int,
                                word_bank: List[int],
                                memo: Optional[Dict[str, int]] = None) -> int:
    """Recursive method for solving problem using custom
    function caching for memoization."""
    count: int = 0
    if memo is None:
        memo: Dict[List[str, int]] = dict()
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            count += count_construct_custom_memo(new_word, word_bank, memo)
    memo[target] = count
    return count


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

assert count_construct_builtin_memo("abcdef", (
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
)) == 1

assert count_construct_builtin_memo("purple", (
    "purp",
    "p",
    "ur",
    "le",
    "purpl",
)) == 2

assert count_construct_builtin_memo("skateboard", (
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
)) == 0

assert count_construct_builtin_memo("enterpotentpot", (
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
)) == 4

assert count_construct_builtin_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", (
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
)) == 0

assert count_construct_custom_memo("abcdef", [
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
]) == 1

assert count_construct_custom_memo("purple", [
    "purp",
    "p",
    "ur",
    "le",
    "purpl",
]) == 2

assert count_construct_custom_memo("skateboard", [
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
]) == 0

assert count_construct_custom_memo("enterpotentpot", [
    "a",
    "p",
    "ent",
    "enter",
    "ot",
    "o",
    "t",
]) == 4

assert count_construct_custom_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
]) == 0
