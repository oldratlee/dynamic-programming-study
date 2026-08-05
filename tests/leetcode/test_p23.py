from collections.abc import Callable

import pytest

from leetcode.p23 import merge_k_sorted_lists, merge_k_sorted_lists_2


@pytest.mark.parametrize("impl", [
    merge_k_sorted_lists, merge_k_sorted_lists_2])
def test_merge_k_sorted_lists(impl: Callable[[list[list[int]]], list[int]]):
    assert impl([]) == []
    assert impl([[]]) == []
    assert impl([[], []]) == []

    assert impl([[1, 3]]) == [1, 3]
    assert impl([[1, 3], []]) == [1, 3]
    assert impl([[], [1, 3]]) == [1, 3]

    assert impl([[2, 4], [1, 3]]) == [1, 2, 3, 4]

    assert impl([
        [1, 4, 5], [1, 3, 4], [2, 6]
    ]) == [1, 1, 2, 3, 4, 4, 5, 6]
