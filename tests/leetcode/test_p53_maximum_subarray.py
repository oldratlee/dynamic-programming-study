import random
from collections.abc import Callable, Sequence

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from leetcode.p53_maximum_subarray import (
    max_nonempty_subarray_sum_accumulate,
    max_nonempty_subarray_sum_brute_force, max_nonempty_subarray_sum_kadane,
    max_subarray_sum_accumulate, max_subarray_sum_brute_force,
    max_subarray_sum_kadane)


@pytest.mark.parametrize("impl", [
    max_subarray_sum_kadane, max_subarray_sum_accumulate,
    max_subarray_sum_brute_force])
def test_max_subarray_sum(impl: Callable[[Sequence[int]], int]):
    assert impl([]) == 0

    assert impl([-1]) == 0
    assert impl([-1, -2]) == 0
    assert impl([-3, -1, -2]) == 0

    assert impl([1]) == 1
    assert impl([5, 4, -1, 7, 8]) == 23
    assert impl([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


@pytest.mark.parametrize("impl", [
    max_nonempty_subarray_sum_kadane, max_nonempty_subarray_sum_accumulate,
    max_nonempty_subarray_sum_brute_force])
def test_max_nonempty_subarray_sum(
        impl: Callable[[Sequence[int]], int | None]):
    assert impl([]) is None

    assert impl([-1]) == -1
    assert impl([-1, -2]) == -1
    assert impl([-3, -1, -2]) == -1

    assert impl([1]) == 1
    assert impl([5, 4, -1, 7, 8]) == 23
    assert impl([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


@pytest.mark.parametrize("impl", [
    max_nonempty_subarray_sum_kadane, max_nonempty_subarray_sum_accumulate,
    max_nonempty_subarray_sum_brute_force])
# n=100 and n=200 keep the brute-force O(n^3) runs within the
# benchmark's time budget while still exposing the speed gaps among
# Kadane O(n), accumulate O(n^2), and brute force O(n^3).
@pytest.mark.parametrize("n", [100, 200])
@pytest.mark.benchmark
def test_benchmark_max_nonempty_subarray_sum(
        benchmark: BenchmarkFixture,
        impl: Callable[[Sequence[int]], int | None], n: int):
    random_list = [random.randrange(-n // 10, n) for _ in range(n)]
    benchmark(impl, random_list)
