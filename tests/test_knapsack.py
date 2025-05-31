from collections.abc import Callable

import pytest

from dynamic_programming_study.knapsack import knapsack, knapsack_memo


@pytest.mark.parametrize("impl", [
    knapsack, knapsack_memo,
])
def test_knapsack(impl: Callable[[list[int], list[int], int], int]):
    assert impl([], [], 5) == 0
    # test case/example in the book
    assert impl([2, 1, 3, 2], [12, 10, 20, 15], 5) == 37
