"""
139. Word Break
https://leetcode.com/problems/word-break

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence
of one or more dictionary words.

Note that the same word in the dictionary may be reused
multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented
as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
* 1 <= s.length <= 300
* 1 <= wordDict.length <= 1000
* 1 <= wordDict[i].length <= 20
* s and wordDict[i] consist of only lowercase English letters.
* All the strings of wordDict are unique.
"""

from collections.abc import Sequence
from functools import cache


def word_break_dp(s: str, word_dict: Sequence[str]) -> bool:
    """
    Determine whether `s` can be segmented into dictionary words.

    Uses dynamic programming: `dp[i]` is True iff the prefix `s[0:i]`
      can be segmented into a sequence of words from `word_dict`.
    Transition: `dp[i] = True` when some word `w` satisfies
      `s[i - len(w):i] == w` and the prefix `s[0:i - len(w)]` is segmentable.

    Complexity (let n = len(s), m = len(word_dict), L = max len(word_dict)):
      Time:  O(n * m * L) - n outer steps × m words × O(L) comparison.
      Space: O(n + L)     - the `dp` array (O(n))
                            plus the temporary slice `s[remain:i]` (O(L)).
    """
    assert all(word_dict)

    # Time O(n): allocate n+1 booleans; Space O(n): the `dp` array
    dp = [False] * (len(s) + 1)

    # Base case: empty str (length 0) can be segmented
    dp[0] = True
    # Main case: check if the substring s[0:i] (length > 0) can be segmented
    #
    # Time O(n): outer steps; Space O(1): loop index only
    for i in range(1, len(s) + 1):
        # Time O(m): inner steps; Space O(1)
        for w in word_dict:
            remain = i - len(w)
            # Time O(L): compare; Space O(L): `s[remain:i]` temp slice
            if remain >= 0 and dp[remain] and s[remain:i] == w:
                dp[i] = True
                break

    return dp[-1]


def word_break_dp_startswith(
        s: str, word_dict: Sequence[str]) -> bool:
    """
    Solve :func:`~p139.word_break_dp` with an optimized substring comparison.

    Identical in logic to :func:`~p139.word_break_dp`,
    except that the substring equality test `s[remain:i] == w`
    is replaced by `s.startswith(w, remain, i)`:

    * `s.startswith(w, remain, i)` checks whether the slice `s[remain:i]`
      begins with ``w``. Since `len(w) == i - remain`, "begins with" is
      equivalent to "equals", so the result is unchanged.
    * The benefit is that :meth:`str.startswith` compares directly against
      the original string without materializing the intermediate slice
      `s[remain:i]`, saving the allocation/copy of a temporary string
      on every inner iteration.

    Complexity (let n = len(s), m = len(word_dict), L = max len(word_dict)):
      Time:  O(n * m * L) - same asymptotic cost as the original:
                            n outer steps × m words × O(L) comparison. Only the
                            constant factor improves (no slice allocation).
      Space: O(n)         - the `dp` array only; `str.startswith` compares
                             in place, so no O(L) temporary slice is allocated
                             (L does not appear in the space bound).
    """
    assert all(word_dict)

    dp = [False] * (len(s) + 1)

    dp[0] = True
    for i in range(1, len(s) + 1):
        for w in word_dict:
            remain = i - len(w)
            # Perform the substring equality test with
            # `s.startswith(w, remain, i)` instead of `s[remain:i] == w`.
            #
            # Time O(L): compare; Space O(1): no temp slice allocated
            if remain >= 0 and dp[remain] and s.startswith(w, remain, i):
                dp[i] = True
                break

    return dp[-1]


def word_break_dfs(s: str, word_dict: Sequence[str]) -> bool:
    """
    Solve :func:`~p139.word_break_dp` by depth-first search (no memoization).

    `go(remaining)` is True iff the suffix `remaining` can be segmented
      into a sequence of words from `word_dict`.
    Transition: `go(remaining) = True` when some word `w` satisfies
      `remaining.startswith(w)` and the leftover suffix
      `remaining[len(w):]` is segmentable.

    Overlapping suffixes are recomputed from scratch, so the call tree
    is exponential in the worst case (contrast the O(n) DP table).

    Complexity (let n = len(s), m = len(word_dict), L = max len(word_dict)):
      Time:  O(2^n * m * L) - up to 2^{n-1} partitions of `s` may be
                              explored; each call tries m words with an
                              O(L) `startswith`.
      Space: O(n^2)         - recursion depth O(n), and each frame holds
                              a suffix copy of length up to n.
    """
    assert all(word_dict)

    def go(s) -> bool:
        # Base case: the empty suffix is already segmented
        if not s:
            return True
        # Try each dictionary word as the next piece of this suffix
        #
        # Time O(m): one startswith (and possibly a recurse) per word
        for w in word_dict:
            # Time O(L): `startswith` compares in place (no prefix slice)
            # Time O(n), Space O(n): `s[len(w):]` copies the leftover suffix
            if s.startswith(w) and go(s[len(w):]):
                return True
        return False

    return go(s)


def word_break_dfs_memo(s: str, word_dict: Sequence[str]) -> bool:
    """
    Solve :func:`~p139.word_break_dp` by depth-first search with memoization
    (top-down DP).

    `go(i)` is True iff the suffix `s[i:]` can be segmented into a
      sequence of words from `word_dict`.
    Transition: `go(i) = True` when some word `w` satisfies
      `s.startswith(w, i)` and `go(i + len(w))` is True.

    Each start index `i` is solved at most once and cached, so overlapping
    suffixes are not recomputed (contrast the exponential uncached search).

    Complexity (let n = len(s), m = len(word_dict), L = max len(word_dict)):
      Time:  O(n * m * L) - n start indices × m words × O(L) `startswith`.
      Space: O(n)         - the memo table of n+1 booleans plus O(n)
                            recursion depth. `str.startswith` compares
                            in place, so no suffix slices are allocated.
    """
    assert all(word_dict)

    @cache
    def go(i: int) -> bool:
        # Base case: the empty suffix (`i == n`) is already segmented
        if i == len(s):
            return True
        # Try each dictionary word as the next piece starting at `i`
        #
        # Time O(m): one startswith (and possibly a recurse) per word
        for w in word_dict:
            # Time O(L): `startswith` compares in place from index `i`
            # Space O(1): no suffix slice; recurse by advancing `i`
            if s.startswith(w, i) and go(i + len(w)):
                return True
        return False

    return go(0)
