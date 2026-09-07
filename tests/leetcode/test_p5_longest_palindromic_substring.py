import random
from collections.abc import Callable

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from leetcode.p5_longest_palindromic_substring import (
    longest_palindromic_substring_brute_force,
    longest_palindromic_substring_dp)


@pytest.mark.parametrize("impl", [
    longest_palindromic_substring_dp,
    longest_palindromic_substring_brute_force])
@pytest.mark.parametrize("s, length", [
    ('', 0),
    ('a', 1),
    # the answer is exactly the final two characters s[n - 2:n] - the
    # last start index of a length-2 substring - so these catch an
    # outer-loop bound that stops one index too early
    ('aa', 2),
    ('abcc', 2),
    ('cbbd', 2),
    ('babad', 3),
    # palindromes of length >= 4: their inner substring is itself a
    # recursive-case cell, so they catch a wrong dp evaluation order
    ('abba', 4),
    ('aaaa', 4),
    ('abcba', 5),
    ('forgeeksskeegfor', 10),
])
def test_longest_palindromic_substring(
        impl: Callable[[str], str], s: str, length: int):
    r = impl(s)
    print(f'\n|{s}| : |{r}|')
    assert r == r[::-1], (s, r, length)
    assert len(r) == length, (s, r, length)


@pytest.mark.parametrize("impl", [
    longest_palindromic_substring_dp,
    longest_palindromic_substring_brute_force])
# n=100 and n=200 keep the brute-force O(n^3) runs within the
# benchmark's time budget while still exposing the speed gap between
# the dp O(n^2) and the brute force O(n^3).
@pytest.mark.parametrize("n", [100, 200])
@pytest.mark.benchmark
def test_benchmark_longest_palindromic_substring(
        benchmark: BenchmarkFixture,
        impl: Callable[[str], str], n: int):
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=n))
    benchmark(impl, random_string)
