"""all_construct_memoization.py"""
from functools import lru_cache
from typing import List, Dict, Optional, Tuple
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


@lru_cache(maxsize=None)
def all_construct_builtin_memo(target: str,
                               word_bank: Tuple[str]) -> List[List[str]]:
    """Recursive method for solving problem using python's
    built-in function caching for memoization. Had to change
    second argument from list to tuple type for hashing."""
    construct_list: List[List[str]] = list()
    if target == "":
        return [[]]
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            construct: List[List[str]] = all_construct_builtin_memo(
                new_word, word_bank)
            constructs: List[List[str]] = [[word] + i for i in construct]
            construct_list += constructs
    return construct_list


def all_construct_custom_memo(
        target: str,
        word_bank: List[str],
        memo: Optional[Dict[str, List[List[str]]]] = None) -> List[List[str]]:
    """Recursive method for solving problem using custom
    function caching for memoization."""
    construct_list: List[List[str]] = list()
    if memo is None:
        memo: Dict[str, List[List[str]]] = dict()
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    for word in word_bank:
        if target.startswith(word):
            new_word: str = target[len(word):]
            construct: List[List[str]] = all_construct_custom_memo(
                new_word, word_bank, memo)
            constructs: List[List[str]] = [[word] + i for i in construct]
            construct_list += constructs
    memo[target] = construct_list
    return construct_list


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
    ["ab", "cd", "ef"],
    ["ab", "c", "def"],
    ["abc", "def"],
    ["abcd", "ef"],
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

assert all_construct_builtin_memo("purple", (
    "purp",
    "p",
    "ur",
    "le",
    "purpl",
)) == [
    ["purp", "le"],
    ["p", "ur", "p", "le"],
]

assert all_construct_builtin_memo("abcdef", (
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
    "ef",
    "c",
)) == [
    ["ab", "cd", "ef"],
    ["ab", "c", "def"],
    ["abc", "def"],
    ["abcd", "ef"],
]

assert all_construct_builtin_memo("skateboard", (
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
)) == []

assert all_construct_builtin_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", (
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
)) == []

assert all_construct_custom_memo("purple", [
    "purp",
    "p",
    "ur",
    "le",
    "purpl",
]) == [
    ["purp", "le"],
    ["p", "ur", "p", "le"],
]

assert all_construct_custom_memo("abcdef", [
    "ab",
    "abc",
    "cd",
    "def",
    "abcd",
    "ef",
    "c",
]) == [
    ["ab", "cd", "ef"],
    ["ab", "c", "def"],
    ["abc", "def"],
    ["abcd", "ef"],
]

assert all_construct_custom_memo("skateboard", [
    "bo",
    "rd",
    "ate",
    "t",
    "ska",
    "sk",
    "boar",
]) == []

assert all_construct_custom_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
]) == []
