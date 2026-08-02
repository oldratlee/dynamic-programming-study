from leetcode.p3 import longest_substring_without_repeating_characters


def test_longest_substring_without_repeating_characters():
    assert longest_substring_without_repeating_characters("") == 0
    assert longest_substring_without_repeating_characters("a") == 1
    assert longest_substring_without_repeating_characters("aa") == 1

    assert longest_substring_without_repeating_characters("abcabcbb") == 3
    assert longest_substring_without_repeating_characters("bbbbb") == 1
    assert longest_substring_without_repeating_characters("pwwkew") == 3
