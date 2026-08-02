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
    max_len = 0

    char_prev_index: dict[str, int] = {}
    cur_longest_len = 0
    for idx, char in enumerate(s):
        cur_longest_len = min(
            idx - char_prev_index.get(char, -1),
            cur_longest_len + 1
        )
        max_len = max(max_len, cur_longest_len)
        char_prev_index[char] = idx

    return max_len
