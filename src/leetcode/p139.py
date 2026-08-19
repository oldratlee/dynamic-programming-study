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


def word_break(s: str, word_dict: Sequence[str]) -> bool:
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


def word_break_opt_substring_comparison(
        s: str, word_dict: Sequence[str]) -> bool:
    """
    Solve :func:`~p139.word_break` with an optimized substring comparison.

    Identical in logic to :func:`~p139.word_break`,
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
