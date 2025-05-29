"""
Change-making problem: Consider the general instance of the following
well-known problem. Give change for amount n using the minimum number of coins
of denominations d1 < d2 < ... < dm. assuming availability of
unlimited quantities of coins for each of
the m denominations d1 < d2 < ... < dm where d1 = 1.

more information see "Introduction to the Design and Analysis
of Algorithms (3rd Ed.)" - Chapter 8.1 - Example 2
"""
from collections.abc import Sequence


def make_change(denominations: Sequence[int], n: int) -> int:
    """
    Returns the minimum number of coins needed
    to make change for a given amount.

    :param denominations: The available coin denominations
    :param n: The target amount of change to make
    :return: The minimum number of coins needed
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = min(dp[i - d] for d in denominations if d <= i) + 1
    return dp[-1]


def make_change_support_d1_absent(
        denominations: Sequence[int], n: int) -> int | None:
    """
    Returns the minimum number of coins needed to make change,
    without requiring denomination 1 to be present in the denominations.

    :param denominations: The available coin denominations
    :param n: The target amount of change to make
    :return: The minimum number of coins needed,
             or None if the amount cannot be made with the given denominations
    """
    dp: list[int | None] = [0] * (n + 1)
    for i in range(1, n + 1):
        candidates = (
            mount + 1  # type: ignore[operator]
            for d in denominations
            if d <= i and (mount := dp[i - d]) is not None)
        dp[i] = min(candidates, default=None)
    return dp[-1]
