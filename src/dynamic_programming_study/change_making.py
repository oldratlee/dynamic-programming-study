"""
Change-making problem: Consider the general instance of the following
well-known problem. Give change for amount n using the minimum number of coins
of denominations d1 < d2 < ... < dm. assuming availability of
unlimited quantities of coins for each of
the m denominations d1 < d2 < . . . < dm where d1 = 1.

more information see "Introduction to the Design and Analysis
of Algorithms (3rd Ed.)" - Chapter 8.1 - Example 2
"""
from collections.abc import Sequence


def change_making(denominations: Sequence[int], n: int) -> int:
    """
    Returns the minimum number of coins of change making

    :param denominations the denominations of coins
    :param n the mount of change
    :return the minimum number of coins
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = min(dp[i - d] for d in denominations if d <= i) + 1
    return dp[-1]
