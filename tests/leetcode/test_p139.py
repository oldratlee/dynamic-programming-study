from leetcode.p139 import word_break


def test_word_break():
    assert word_break("", [])
    assert word_break("", ["leet", "code"])
    assert not word_break("foo", [])

    assert word_break("leetcode", ["leet", "code"])
    assert word_break("applepenapple", ["apple", "pen"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
