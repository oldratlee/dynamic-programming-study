"""
Coin-collecting problem: Several coins are placed in cells of an n × m board,
no more than one coin per cell. A robot, located in the upper left cell
of the board, needs to collect as many of the coins as possible and bring them
to the bottom right cell. On each step, the robot can move either one cell
to the right or one cell down from its current location. When the robot
visits a cell with a coin, it always picks up that coin.
Design an algorithm to find the maximum number of coins the robot
can collect and a path it needs to follow to do this.

more information see "Introduction to the Design and Analysis
of Algorithms (3rd Ed.)" - Chapter 8.1 - Example 3
"""
from collections.abc import Sequence
from itertools import product
from typing import Final


def collect_coin(board: Sequence[Sequence[bool]]) -> int:
    if not board:
        return 0
    m: Final[int] = len(board)
    if not board[0]:
        return 0
    n: Final[int] = len(board[0])

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i, j in product(range(1, m + 1), range(1, n + 1)):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + board[i - 1][j - 1]
    return dp[-1][-1]
