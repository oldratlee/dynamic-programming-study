from collections.abc import Callable, Sequence

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from leetcode.p139 import (word_break_dfs, word_break_dfs_memo, word_break_dp,
                           word_break_dp_startswith)


@pytest.mark.parametrize("impl", [
    word_break_dp, word_break_dp_startswith,
    word_break_dfs, word_break_dfs_memo])
def test_word_break(impl: Callable[[str, Sequence[str]], bool]):
    assert impl("", [])
    assert impl("", ["leet", "code"])
    assert not impl("foo", [])

    assert impl("leetcode", ["leet", "code"])
    assert impl("applepenapple", ["apple", "pen"])
    assert not impl("catsandog", ["cats", "dog", "sand", "and", "cat"])


@pytest.mark.parametrize("impl", [
    word_break_dp, word_break_dp_startswith,
    word_break_dfs, word_break_dfs_memo])
# Many overlapping partitions of a run of `a`s: exponential without memo.
@pytest.mark.parametrize("s, expected", [
    ("a" * 12, True),
    ("a" * 12 + "b", False),
])
@pytest.mark.benchmark
def test_benchmark_word_break(
        benchmark: BenchmarkFixture,
        impl: Callable[[str, Sequence[str]], bool],
        s: str, expected: bool):
    assert benchmark(impl, s, ["a", "aa", "aaa", "aaaa"]) is expected
