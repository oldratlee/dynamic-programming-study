"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string s, find the length of the longest substring
without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.

Constraints:
* 0 <= s.length <= 105
* s consists of English letters, digits, symbols and spaces.
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    # max_len: the global maximum length of a substring without repeating
    #          characters found so far across the entire string.
    # cur_longest_len: the length of the longest non-repeating substring
    #                  that *ends* at the current index being processed.
    max_len = cur_longest_len = 0
    # char_prev_index: a hash map storing the most recent index at which each
    #                  character was seen. Used to detect duplicates and to
    #                  know where the current window must start (or shrink to).
    char_prev_index: dict[str, int] = {}
    for idx, char in enumerate(s):
        # Determine the length of the longest non-repeating substring ending
        # at `idx`. Two constraints bound this length, so we take the smaller:
        #
        # 1. idx - char_prev_index.get(char, -1):
        #    If `char` was seen before at index `prev`, then any substring
        #    ending at `idx` that includes `char` can only start *after* `prev`
        #    (otherwise `char` would appear twice). So the window cannot be
        #    longer than the distance from `prev` to `idx`.
        #    If `char` has never been seen, `.get(char, -1)` returns -1, making
        #    this value `idx + 1` (the entire prefix up to `idx`), which is
        #    effectively unbounded so the other constraint will win.
        #
        # 2. cur_longest_len + 1:
        #    The previous window (ending at `idx - 1`) had length
        #    `cur_longest_len`. We can extend it by at most 1 (the new char).
        #    This prevents the window from growing unboundedly when there is
        #    no duplicate — it simply grows one character at a time.
        #
        # Taking the min ensures we respect whichever constraint is tighter.
        cur_longest_len = min(
            idx - char_prev_index.get(char, -1),
            cur_longest_len + 1
        )
        max_len = max(cur_longest_len, max_len)
        # Record this character's current index so future occurrences can
        # reference it to shrink the window when a duplicate is found.
        char_prev_index[char] = idx

    return max_len
