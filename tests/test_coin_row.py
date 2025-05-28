from collections.abc import Callable, Sequence

import pytest

from dynamic_programming_study.coin_row import (coin_row_conventional,
                                                coin_row_optimise_states_space)


@pytest.mark.parametrize("impl", [
    coin_row_conventional, coin_row_optimise_states_space,
])
def test_coin_row(impl: Callable[[Sequence[int]], int]):
    assert impl(tuple()) == 0
    assert impl([]) == 0

    assert impl((1,)) == 1
    assert impl([42]) == 42

    assert impl([1, 2]) == 2
    assert impl([2, 1]) == 2

    assert impl([1, 2, 3]) == 4
    assert impl([1, 10, 3]) == 10

    assert impl([1, 2, 3, 10]) == 12
    assert impl([1, 1, 3, 1]) == 4

    assert impl([40, 1, 3, 60]) == 100

    # test case/example in the book
    assert impl([5, 1, 2, 10, 6, 2]) == 17
    assert impl([5, 1, 2, 10, 6]) == 15
    assert impl([5, 1, 2, 10]) == 15
    assert impl([5, 1, 2]) == 7
    assert impl([5, 1]) == 5
    assert impl([5]) == 5
