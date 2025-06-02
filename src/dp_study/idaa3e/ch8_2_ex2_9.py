from collections.abc import Sequence
from itertools import product


def longest_common_subsequence_length(a: Sequence, b: Sequence) -> int:
    """
    find the length of the longest common subsequence in two sequences

    more information see "Introduction to the Design and Analysis
    of Algorithms (3rd Ed.)" - Chapter 8.2 Exercises 8.2 Problem 9
    """
    if not a or not b:
        return 0

    dp: list[list[int]] = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, j in product(range(1, len(a) + 1), range(1, len(b) + 1)):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + (a[i - 1] == b[j - 1])
    return dp[-1][-1]


def longest_common_subsequence[T](
        a: Sequence[T], b: Sequence[T]) -> Sequence[T]:
    """
    find the longest common subsequence in two sequences

    more information see "Introduction to the Design and Analysis
    of Algorithms (3rd Ed.)" - Chapter 8.2 Exercises 8.2 Problem 9
    """
    if not a or not b:
        return []

    dp: list[list[list[T]]] = [[[]] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, j in product(range(1, len(a) + 1), range(1, len(b) + 1)):
        append_element = [a[i - 1]] * (a[i - 1] == b[j - 1])
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len) + append_element
    return dp[-1][-1]
