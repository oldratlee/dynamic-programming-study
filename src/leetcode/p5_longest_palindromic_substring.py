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

Implementation Note:
* the implementations deliberately also accept the empty string -
  outside the constraint above - and return '' for it; the tests cover it.
* When several substrings tie for the longest, any one of them may be returned:
  the implementations in this module may pick different winners on ties
  (for "babad" this DP returns "aba" while expand-around-center returns "bab"),
  so tests assert the length and palindromicity of the result,
  not its exact value.
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
    loop iterates `start` in descending order.

    Complexity (let n = len(s)):
      Time:  O(n^2) - n * (n + 1) table cells, each filled in O(1).
                      The winning slice `s[start:stop]` is copied only when
                      a strictly longer palindrome appears (at most n times,
                      O(n) each), which stays within O(n^2).
      Space: O(n^2) - the `dp` table of n rows x (n + 1) booleans.
    """
    # `max_len`/`candidate` track the longest palindrome seen so far.
    # Seed with the empty string (length 0).
    max_len, candidate = 0, ''

    n = len(s)
    # dp[start][stop] == True iff s[start:stop] is a palindrome.
    # `stop` is exclusive, so each row has n + 1 cells (stop may equal n).
    #
    # Time O(n^2): allocate the table; Space O(n^2): the table itself
    dp = [[False] * (n + 1) for _ in range(n)]
    # Base cases: the empty substring s[i:i] and every single character
    # s[i:i + 1] are palindromic.
    for i in range(n):
        dp[i][i] = dp[i][i + 1] = True
        # Promote the seed to a single character:
        #   every single character is a palindrome.
        # the recursive-case loop below only tracks length >= 2,
        # so without this an input like "ab" (whose longest palindrome
        # is a single character) would wrongly return ''.
        if 1 > max_len:
            max_len, candidate = 1, s[i]
    # Recursive case: substrings of length >= 2; the empty and
    # single-character substrings are the base cases handled above.
    #
    # `start` iterates from n - 2 down to 0.
    #   - `reversed(range(n - 1))`.
    #   - `n - 2` is the last index a length-2 substring can start at.
    # `stop` runs from `start + 2` (length 2) through `n`.
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
                if (length := stop - start) > max_len:
                    # Time O(n): copy the slice
                    max_len, candidate = length, s[start:stop]

    return candidate


def longest_palindromic_substring_expand_around_center(s: str) -> str:
    """
    Space-optimized counterpart of :func:`longest_palindromic_substring_dp`:
    expand palindromes outward from every center instead of tabulating
    all substrings ("expand around center", the name of this approach
    in the LeetCode editorial for problem 5).

    A palindrome is mirror-symmetric, so it is fully determined by its
      center. `s` has exactly `2n - 1` centers: `n` on characters
      (odd-length palindromes) and `n - 1` on the gaps between adjacent
      characters (even-length palindromes). Each center is seeded with
      the shortest palindrome there - the character `s[center:center + 1]`
      or the empty span `s[center:center]` on the gap just before
      character `center` - and then expand outwards.
    Transition: a palindromic span `[start, stop)` (half-open, the same
      slice convention as the DP's `dp[start][stop]`) extends to
      `[start - 1, stop + 1)` while `start > 0`, `stop < n` and
      `s[start - 1] == s[stop]`. `s[start:stop]` is palindromic before
      the loop, after every step and at exit, so the span left when the
      first extension fails is itself the longest palindrome at that
      center - no post-loop index fixup is needed.

    Unlike the DP, no result is shared between centers - each expansion
      re-compares characters the DP would read from a table in O(1).
      The payoff is that the O(n^2) table disappears and the constant
      factor drops (no table allocation, better memory locality).

    Complexity (let n = len(s)):
      Time:  O(n^2) - 2n - 1 centers, each expanded at most n / 2 steps
                      of O(1) character comparison. Same asymptotic
                      bound as the DP but a much smaller constant;
                      typical inputs finish far below the worst case
                      (all characters equal).
      Space: O(1)   - scalar bookkeeping only; the answer slice is copied once
                      at the very end and is the output itself,
                      not working memory (contrast the DP's O(n^2) table).

    References:
      * LeetCode editorial for problem 5, Approach 4 "Expand Around Center"
        (O(n^2) time, O(1) space, as here):
        https://leetcode.com/problems/longest-palindromic-substring/editorial/
      * GeeksforGeeks "Longest Palindromic Substring" - includes a section
        titled "Expand Around Center":
        https://www.geeksforgeeks.org/longest-palindromic-substring/
      * Wikipedia "Longest palindromic substring" - presents this
        per-center expansion as the straightforward O(n^2) method and
        Manacher's algorithm (Manacher, 1975) as the O(n) improvement:
        https://en.wikipedia.org/wiki/Longest_palindromic_substring
      * cp-algorithms "Manacher's Algorithm" - treats this per-center
        expansion as the O(n^2) baseline that Manacher improves on:
        https://cp-algorithms.com/string/manacher.html
    """
    n = len(s)
    # Longest palindrome found so far, kept as its start index and length.
    # Seed with the empty string (length 0).
    # for s == '' the loop never runs, so s[0:0] returns ''.
    best_start, max_len = 0, 0

    for center in range(n):
        # An odd-length palindrome is centered on the character `center`,
        # an even-length one on the gap just before character `center`
        # (between `center - 1` and `center`).
        # Both seeds are half-open spans: the odd seed s[center:center + 1] is
        # the character itself (length 1), the even seed s[center:center]
        # the empty span on that gap (length 0).
        # For center == 0 that "gap" is the string boundary, so the even seed
        # never expands - a harmless no-op that keeps the loop uniform.
        for start, stop in ((center, center), (center, center + 1)):
            # Invariant: s[start:stop] is a palindrome. Each step compares
            # the characters just outside the span, s[start - 1] and
            # s[stop], and absorbs them when they match, so the span only
            # ever holds valid palindromes. Time O(1) per step; at most
            # n / 2 steps per seed.
            while start > 0 and stop < n and s[start - 1] == s[stop]:
                start -= 1
                stop += 1
            if (length := stop - start) > max_len:
                best_start, max_len = start, length

    # Time O(n): materialize the winning slice exactly once.
    return s[best_start:best_start + max_len]


def longest_palindromic_substring_brute_force(s: str) -> str:
    """
    Brute-force counterpart of :func:`longest_palindromic_substring_dp`:
    enumerate every substring and keep the longest one that reads the
    same forwards and backwards.

    Enumerates every substring `s[start:stop]` of length >= 1 and tests
    each candidate against its own reversal.

    Complexity (let n = len(s)):
      Time:  O(n^3) - O(n^2) substrings, each sliced, reversed and
                      compared in O(length). The `length <= max_len`
                      prune skips hopeless candidates in O(1) but does
                      not change the worst case.
      Space: O(n)   - the temporary slice `sub` and its reversal
                      `sub[::-1]` each hold up to n characters.
    """
    # Seed with the empty string (length 0).
    max_len, candidate = 0, ''
    # Enumerate every substring s[start:stop] of length >= 1.
    #   start: inclusive left index, running from 0 up to `len(s) - 1`
    #          (the last character).
    #   stop:  exclusive right index, running from `start + 1` (length 1)
    #          up to `len(s)` (the whole suffix).
    for start in range(len(s)):
        for stop in range(start + 1, len(s) + 1):
            if (length := stop - start) <= max_len:
                continue
            # Time O(length): slice + reversal + comparison;
            # Space O(length): the temporary slice `sub` and `sub[::-1]`
            if (sub := s[start:stop]) == sub[::-1]:
                max_len, candidate = length, sub
    return candidate
