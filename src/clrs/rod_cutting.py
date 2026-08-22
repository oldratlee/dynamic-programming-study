"""
Rod Cutting
Introduction to Algorithms (4th Ed.) — Chapter 14

Given a rod of length n and a table of prices `prices[i]` for a rod of
length i (with `prices[0] = 0`), determine the maximum revenue obtainable
by cutting up the rod and selling the pieces.

Example (CLRS Figure 14.1):
Input:  prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        (rod length n = 10)
Output: 30
Explanation: Selling the rod uncut yields 30, which is optimal.
             Other lengths admit better cuts, e.g. n = 4 → cut into
             2 + 2 for revenue 5 + 5 = 10 > prices[4] = 9.
"""


def cut_rod(prices: list[int]) -> int:
    """
    Maximum revenue from cutting a rod of length `n = len(prices) - 1`,
    using bottom-up dynamic programming (CLRS BOTTOM-UP-CUT-ROD).

    `prices[i]` is the market price of an uncut rod of length i;
    `prices[0]` must be 0.

    Time : O(n²)  — for each rod length we try every first-cut position j.
    Space: O(n)   — one DP table of size n + 1.
    """
    assert prices[0] == 0

    # n: length of the rod we are pricing (prices is 1-indexed by length).
    n = len(prices) - 1
    # dp[length]: maximum revenue obtainable from a rod of that length.
    # dp[0] = 0 — a rod of length 0 is worthless.
    dp = [0] * (n + 1)

    # length: the rod size whose optimal revenue we fill in this iteration.
    #   Solved bottom-up from 1..n so every smaller piece is already known.
    for length in range(1, n + 1):
        # Optimal revenue for this length is the best among:
        #
        # 1. Split into two positive-length pieces j and length - j
        #    (j = 1..length-1), each already solved optimally:
        #      dp[j] + dp[length - j]
        #    When length = 1 the range is empty, so max(..., default=0)
        #    yields 0 — a unit rod has no two-piece split. Because every
        #    further cut is already folded into dp[j] / dp[length-j], this
        #    covers all multi-piece partitions.
        #
        # 2. Sell the rod of this length uncut at prices[length].
        #
        # Taking the max of (1) and (2) is the rod-cutting recurrence.
        dp[length] = max((
            dp[j] + dp[length - j] for j in range(1, length)
        ), default=0)
        dp[length] = max(dp[length], prices[length])
    return dp[-1]


def cut_rod_price_seeded(prices: list[int]) -> int:
    """
    Same problem as `cut_rod`, but seed the DP table with the market prices
    so selling a rod uncut is the baseline and needs no separate `max`.

    `dp` starts as a copy of `prices`. For each length we then replace
    `dp[length]` with the best of every split `dp[j] + dp[length - j]`
    (including j = 0, which recovers the uncut price via
    `dp[0] + dp[length]` while `dp[length]` is still the seeded value).

    Time : O(n²)  — for each rod length we try every split position j.
    Space: O(n)   — one DP table of size n + 1 (a copy of `prices`).
    """
    assert prices[0] == 0

    # dp[length]: best revenue for that length so far.
    # Seeded with prices[length] — the revenue from selling uncut,
    #   so the uncut option is already present before we consider any cuts.
    dp = prices[:]

    # length: the rod size whose optimal revenue we improve this iteration.
    #         Solved bottom-up from 1..n so every smaller piece is already
    #         optimal (not merely its uncut price).
    for length in range(1, len(prices)):
        # Recompute dp[length] as the best split into pieces j and length - j.
        # j runs from 0..length-1 (j = length would duplicate j = 0):
        #   - j = 0 → dp[0] + dp[length] = prices[length]
        #     (still the seeded uncut value at evaluation time), so uncut
        #     stays in the candidate set without an explicit prices[length].
        #   - j = 1..length-1 → combine two already-optimal shorter rods.
        dp[length] = max(dp[j] + dp[length - j] for j in range(length))
    return dp[-1]
