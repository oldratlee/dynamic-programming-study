from collections.abc import Callable, Sequence

import pytest

from dp_study.idaa3e.ch8_2_knapsack import knapsack, knapsack_memo


@pytest.mark.parametrize("impl", [
    knapsack, knapsack_memo])
def test_knapsack(impl: Callable[[Sequence[int], Sequence[int], int], int]):
    assert impl([], [], 5) == 0
    # test case/example in the book
    assert impl([2, 1, 3, 2], [12, 10, 20, 15], 5) == 37
