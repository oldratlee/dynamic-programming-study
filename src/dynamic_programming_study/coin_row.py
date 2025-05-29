"""
Coin-row problem: There is a row of n coins whose values are
some positive integers c1, c2, ... , cn, not necessarily distinct.
The goal is to pick up the maximum amount of money subject to
the constraint that no two coins adjacent in the initial row can be picked up.

more information see "Introduction to the Design and Analysis
of Algorithms (3rd Ed.)" - Chapter 8.1 - Example 1
"""
from collections.abc import Sequence


def coin_row_conventional(coins: Sequence[int]) -> int:
    """
    Solves the coin row problem using a conventional approach by the book.
    """
    if not coins:
        return 0

    dp = [0] * (len(coins) + 1)
    dp[1] = coins[0]
    for i in range(2, len(coins) + 1):
        dp[i] = max(dp[i - 2] + coins[i - 1], dp[i - 1])
    return dp[-1]


def coin_row_optimise_states_space(coins: Sequence[int]) -> int:
    """
    Optimizes space complexity by only storing the previous two states,
    since computing the next state only requires the last two results.
    """
    if not coins:
        return 0

    previous, current = 0, coins[0]
    for i in range(1, len(coins)):
        previous, current = current, max(previous + coins[i], current)
    return current
