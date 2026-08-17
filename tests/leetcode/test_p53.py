from collections.abc import Callable, Sequence

import pytest

from leetcode.p53 import (max_nonempty_subarray_sum,
                          max_nonempty_subarray_sum_brute_force,
                          max_subarray_sum, max_subarray_sum_brute_force)


@pytest.mark.parametrize("impl", [
    max_subarray_sum, max_subarray_sum_brute_force])
def test_max_subarray_sum(impl: Callable[[Sequence[int]], int]):
    assert impl([]) == 0

    assert impl([-1]) == 0
    assert impl([-1, -2]) == 0
    assert impl([-3, -1, -2]) == 0

    assert impl([1]) == 1
    assert impl([5, 4, -1, 7, 8]) == 23
    assert impl([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


@pytest.mark.parametrize("impl", [
    max_nonempty_subarray_sum, max_nonempty_subarray_sum_brute_force])
def test_max_nonempty_subarray_sum(
        impl: Callable[[Sequence[int]], int | None]):
    assert impl([]) is None

    assert impl([-1]) == -1
    assert impl([-1, -2]) == -1
    assert impl([-3, -1, -2]) == -1

    assert impl([1]) == 1
    assert impl([5, 4, -1, 7, 8]) == 23
    assert impl([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
