"""
Knapsack Problem: Given n items of known weights w1, w2, ... , wn
and values v1, v2, ... , vn and a knapsack of capacity W,
find the most valuable subset of the items that fit into the knapsack.

more information see "Introduction to the Design and Analysis
of Algorithms (3rd Ed.)" - Chapter 3.4 / 8.2
"""
from collections.abc import Sequence
from functools import cache
from itertools import product


def knapsack(item_weights: Sequence[int], item_values: Sequence[int],
             capacity: int) -> int:
    if not item_weights:
        return 0

    dp = [[0] * (len(item_weights) + 1) for _ in range(capacity + 1)]
    for c, i in product(range(1, capacity + 1),
                        range(1, len(item_weights) + 1)):
        if (c_minus := c - item_weights[i - 1]) >= 0:
            dp[c][i] = max(dp[c][i - 1],
                           dp[c_minus][i - 1] + item_values[i - 1])
        else:
            dp[c][i] = dp[c][i - 1]
    return dp[-1][-1]


def knapsack_memo(item_weights: list[int], item_values: list[int],
                  capacity: int) -> int:
    @cache
    def go(c, i):
        """
        :param c: remaining capacity
        :param i: the item number to be used
        """
        if c == 0 or i == 0:
            return 0
        elif (c_minus := c - item_weights[i - 1]) >= 0:
            return max(go(c, i - 1), go(c_minus, i - 1) + item_values[i - 1])
        else:
            return go(c, i - 1)

    return go(capacity, len(item_weights))
