from collections.abc import Callable, Sequence

import pytest

from leetcode.p139 import word_break, word_break_opt_substring_comparison


@pytest.mark.parametrize("impl", [
    word_break, word_break_opt_substring_comparison])
def test_word_break(impl: Callable[[str, Sequence[str]], bool]):
    assert impl("", [])
    assert impl("", ["leet", "code"])
    assert not impl("foo", [])

    assert impl("leetcode", ["leet", "code"])
    assert impl("applepenapple", ["apple", "pen"])
    assert not impl("catsandog", ["cats", "dog", "sand", "and", "cat"])
