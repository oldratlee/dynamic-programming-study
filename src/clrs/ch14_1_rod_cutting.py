"""
Rod Cutting
Introduction to Algorithms (4th Ed.) — Chapter 14

Given a rod of length n and a table of prices `prices[i]` for a rod of
length i + 1, determine the maximum revenue obtainable by cutting up
the rod and selling the pieces.

Example (CLRS Figure 14.1, without the book's `prices[0] = 0` sentinel):
Input:  prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        (rod length n = 10)
Output: 30
Explanation: Selling the rod uncut yields 30, which is optimal.
             Other lengths admit better cuts, e.g. n = 4 → cut into
             2 + 2 for revenue 5 + 5 = 10 > prices[3] = 9.
"""


def cut_rod_split(prices: list[int]) -> int:
    """
    Maximum revenue from cutting a rod of length `n = len(prices)`,
    combining two already-optimal pieces (bottom-up).

    `prices[i]` is the market price of an uncut rod of length i + 1.
    An empty `prices` list is a rod of length 0 and yields 0.

    Time : O(n²)  — for each rod length we try every first-cut position j.
    Space: O(n)   — one DP table of size n.
    """
    if not prices:
        return 0

    # n: length of the rod we are pricing.
    # prices[i] is 0-indexed by length: it is the uncut price of a rod
    # of length i + 1 (no CLRS-style prices[0] = 0 sentinel).
    n = len(prices)
    # dp[i]: maximum revenue obtainable from a rod of length i + 1.
    # dp[0] = prices[0] — a unit rod cannot be split.
    dp = [0] * n
    dp[0] = prices[0]

    # i: 0-based index of the rod of length i + 1 whose optimal revenue
    #    we fill this iteration. Solved bottom-up from length 2..n so
    #    every shorter piece is already known.
    for i in range(1, n):
        # Optimal revenue for a rod of length i + 1 is the best among:
        #
        # 1. Split into two positive-length pieces of lengths j + 1 and
        #    (i + 1) - (j + 1) = i - j, each already solved optimally:
        #      dp[j] + dp[i - j - 1]
        #    j runs through 0..i-1, i.e. every two-piece split. Because
        #    every further cut is already folded into those two
        #    subproblems, this covers all multi-piece partitions.
        #
        # 2. Sell the rod of this length uncut at prices[i].
        #
        # Taking the max of (1) and (2) is the rod-cutting recurrence.
        length = i + 1
        # Second piece has length `length - (j + 1)`, stored at 0-based
        # index `i - j - 1 (= length - (j + 1) - 1)`.
        dp[i] = max(dp[j] + dp[i - j - 1] for j in range(length - 1))
        dp[i] = max(dp[i], prices[i])
    return dp[-1]


def cut_rod_split_seeded(prices: list[int]) -> int:
    """
    Same problem as `cut_rod_split`, but seed the DP table with the market
    prices so selling a rod uncut is the baseline and needs no separate `max`.

    Builds a 1-indexed table `dp` with `dp[0] = 0` and `dp[1:] = prices`,
    so `dp[length]` starts as the uncut price of a rod of that length.
    For each length ≥ 2 we then replace `dp[length]` with the best of
    every split `dp[j] + dp[length - j]` (including j = 0, which recovers
    the uncut price via `dp[0] + dp[length]` while `dp[length]` is still
    the seeded value).

    Time : O(n²)  — for each rod length we try every split position j.
    Space: O(n)   — one DP table of size n + 1.
    """
    # dp[length]: best revenue for a rod of that length so far.
    # dp[0] = 0; dp[1:] is seeded with prices — the uncut revenue —
    # so the uncut option is already present before we consider any cuts.
    dp = [0] * (len(prices) + 1)
    dp[1:] = prices

    # length: the rod size whose optimal revenue we improve this iteration.
    #         Starts at 2 (a unit rod has no split). Solved bottom-up so
    #         every smaller piece is already optimal (not merely uncut).
    for length in range(2, len(dp)):
        # Recompute dp[length] as the best split into pieces j and length - j.
        # j runs from 0..length-1 (j = length would duplicate j = 0):
        #   - j = 0 → dp[0] + dp[length] = seeded uncut price
        #     (still the original prices[length - 1] at evaluation time),
        #     so uncut stays in the candidate set without an extra max.
        #   - j = 1..length-1 → combine two already-optimal shorter rods.
        dp[length] = max(dp[j] + dp[length - j] for j in range(length))
    return dp[-1]


def cut_rod_first_cut(prices: list[int]) -> int:
    """
    Maximum revenue from cutting a rod of length `n = len(prices)`,
    choosing an uncut first piece and an already-optimal remainder
    (bottom-up).

    `prices[i]` is the market price of an uncut rod of length i + 1.
    An empty `prices` list is a rod of length 0 and yields 0.

    This is the CLRS first-cut recurrence: a first piece of length j is
    sold uncut at `prices[j - 1]`, and the leftover rod of length n - j
    is solved optimally. j = n sells the whole rod uncut.

    Time : O(n²)  — for each rod length we try every first-cut length j.
    Space: O(n)   — one DP table of size n.
    """
    if not prices:
        return 0

    # n: length of the rod we are pricing.
    # prices[i] is 0-indexed by length: it is the uncut price of a rod
    # of length i + 1 (no CLRS-style prices[0] = 0 sentinel).
    n = len(prices)
    # dp[i]: maximum revenue obtainable from a rod of length i + 1.
    # dp[0] = prices[0] — a unit rod cannot be split.
    dp = [0] * n
    dp[0] = prices[0]

    # i: 0-based index of the rod of length i + 1 whose optimal revenue
    #    we fill this iteration. Solved bottom-up from length 2..n so
    #    every shorter remainder is already known.
    for i in range(1, n):
        # Optimal revenue for a rod of length i + 1 is the best first cut:
        #
        # Cut off a first piece of length j (j = 1..length) and sell it
        # uncut at prices[j - 1]; the remainder of length length - j is
        # already optimal at dp[length - j - 1].
        #
        # j = length sells the whole rod uncut. The remainder index
        # length - j - 1 is then -1; in Python that is dp[-1], still 0
        # at evaluation time (the slot being written, or a later unfilled
        # slot), so the candidate is just prices[length - 1].
        length = i + 1
        dp[i] = max(prices[j - 1] + dp[length - j - 1]
                    for j in range(1, length + 1))
    return dp[-1]


def cut_rod_first_cut_1indexed(prices: list[int]) -> int:
    """
    Same problem as `cut_rod_first_cut`, but with a 1-indexed DP table
    so the remainder of length 0 is an explicit `dp[0] = 0` sentinel.

    `dp[length]` is the maximum revenue for a rod of that length.
    The recurrence is the CLRS first-cut form:
        dp[length] = max_{1 ≤ j ≤ length} prices[j - 1] + dp[length - j]
    including j = length, which is the uncut option via `dp[0]`.

    An empty `prices` list leaves `dp = [0]` and yields 0.

    Time : O(n²)  — for each rod length we try every first-cut length j.
    Space: O(n)   — one DP table of size n + 1.
    """
    # dp[length]: maximum revenue for a rod of that length.
    # dp[0] = 0 — a rod of length 0 contributes nothing, and lets
    # j = length (sell uncut) be prices[length - 1] + dp[0].
    dp = [0] * (len(prices) + 1)

    # length: the rod size whose optimal revenue we fill this iteration.
    #         Solved bottom-up from 1..n so every shorter remainder
    #         is already known. Length 1 is just prices[0] + dp[0].
    for length in range(1, len(dp)):
        # First cut of length j sold uncut; remainder length - j already
        # optimal. j = 1..length:
        #   - j < length → prices[j - 1] + dp[length - j]
        #   - j = length → prices[length - 1] + dp[0]  (uncut)
        dp[length] = max(prices[j - 1] + dp[length - j]
                         for j in range(1, length + 1))
    return dp[-1]
