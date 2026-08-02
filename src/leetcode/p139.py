"""
139. Word Break
https://leetcode.com/problems/word-break/description/

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
    # Dynamic programming state explanation:
    #   dp[i] indicates whether the substring s[0:i] (of length `i`)
    #   can be segmented into the words from the dictionary.
    dp = [False] * (len(s) + 1)

    # Base case: an empty string (length 0) can always be segmented
    dp[0] = True
    # Main case: check if the substring s[0:i] (length i, where i > 0) can be segmented
    for i in range(1, len(s) + 1):
        for w in word_dict:
            remain = i - len(w)
            if remain >= 0 and dp[remain] and s[remain:i] == w:
                dp[i] = True
                continue

    return dp[-1]
