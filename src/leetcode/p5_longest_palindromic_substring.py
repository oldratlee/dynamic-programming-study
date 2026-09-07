"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
* 1 <= s.length <= 1000
* s consist of only digits and English letters.
"""


def longest_palindromic_substring_dp(s: str) -> str:
    """
    Return the longest palindromic substring of `s`.

    Uses dynamic programming over substrings: `dp[start][stop]` is True
      iff the substring `s[start:stop]` is a palindrome.
    Transition: `dp[start][stop]` is True when the two ends match
      (`s[start] == s[stop - 1]`) and the inner substring is itself a
      palindrome (`dp[start + 1][stop - 1]`, i.e. `s[start + 1:stop - 1]`).

    The transition reads a cell with a *larger* `start`, so the outer
    loop iterates `start` in descending order; every dependency is then
    already filled when it is read. A substring of length >= 2 needs
    two characters, so `start` never exceeds n - 2.

    Complexity (let n = len(s)):
      Time:  O(n^2) - n * (n + 1) table cells, each filled in O(1).
                      The winning slice `s[start:stop]` is copied only when
                      a strictly longer palindrome appears (at most n times,
                      O(n) each), which stays within O(n^2).
      Space: O(n^2) - the `dp` table of n rows x (n + 1) booleans.
    """
    if not s:
        return ''

    n = len(s)
    # dp[start][stop] == True iff s[start:stop] is a palindrome.
    # `stop` is exclusive, so each row has n + 1 cells (stop may equal n).
    #
    # Time O(n^2): allocate the table; Space O(n^2): the table itself
    dp = [[False] * (n + 1) for _ in range(n)]

    # `max_len`/`candidate` track the longest palindrome seen so far.
    # Length 1 substrings are always palindromic, so seed with s[0].
    max_len, candidate = 1, s[0]

    # Base cases: the empty substring s[i:i] and every single letter
    # s[i:i + 1] are palindromic.
    for i in range(n):
        dp[i][i] = True
        dp[i][i + 1] = True
    # Recursive case: substrings of length >= 2; the empty and
    # single-letter substrings are the base cases handled above.
    # Length >= 2 requires `stop >= start + 2`, which combined with
    # `stop <= n` caps `start` at n - 2 - hence `range(n - 1)`.
    #
    # The transition reads dp[start + 1][stop - 1] - a cell with a larger
    # `start` - so iterate `start` in descending order to ensure the
    # dependency is computed before it is read. Ascending order would
    # leave every palindrome of length >= 4 undetected.
    for start in reversed(range(n - 1)):
        for stop in range(start + 2, n + 1):
            # s[start:stop] is palindromic iff its ends match and the
            # inner substring s[start + 1:stop - 1] is palindromic.
            if s[start] == s[stop - 1] and dp[start + 1][stop - 1]:
                dp[start][stop] = True
                # Time O(n): copy the slice, but only when it strictly
                # improves `max_len` (at most n times in total)
                if (length := stop - start) > max_len:
                    max_len, candidate = length, s[start:stop]

    return candidate


def longest_palindromic_substring_brute_force(s: str) -> str:
    """
    Brute-force counterpart of :func:`longest_palindromic_substring_dp`:
    enumerate every substring and keep the longest one that reads the
    same forwards and backwards.

    Enumerates every substring `s[start:stop]` of length >= 2 (length-1
    substrings are already covered by the initial `candidate = s[0]`)
    and tests each candidate against its own reversal. A substring of
    length >= 2 needs two characters, so `start` never exceeds
    len(s) - 2.

    Complexity (let n = len(s)):
      Time:  O(n^3) - O(n^2) substrings, each sliced, reversed and
                      compared in O(length). The `length <= max_len`
                      prune skips hopeless candidates in O(1) but does
                      not change the worst case.
      Space: O(n)   - the temporary slice `sub` and its reversal
                      `sub[::-1]` each hold up to n characters.
    """
    if not s:
        return ''

    # single letter substrings are always palindromic, so seed with s[0].
    max_len, candidate = 1, s[0]
    # Enumerate every substring s[start:stop] of length >= 2; anything
    # shorter is trivially palindromic and cannot improve on the seed.
    #   start: inclusive left index, 0 .. len(s) - 2. Length >= 2
    #          requires `stop >= start + 2`, which combined with
    #          `stop <= len(s)` caps `start` at len(s) - 2.
    #   stop:  exclusive right index, running from `start + 2` (length 2)
    #          up to `len(s)` (the whole suffix).
    for start in range(len(s) - 1):
        for stop in range(start + 2, len(s) + 1):
            # Prune: only substrings strictly longer than the current
            # best can become the new answer.
            if (length := stop - start) <= max_len:
                continue
            # Time O(length): slice + reversal + comparison;
            # Space O(length): the temporary slice `sub` and `sub[::-1]`
            if (sub := s[start:stop]) == sub[::-1]:
                max_len, candidate = length, sub
    return candidate
