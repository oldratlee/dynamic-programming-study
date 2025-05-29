from collections.abc import Callable, Sequence

import pytest

from dynamic_programming_study.change_making import (
    change_making, change_making_support_d1_absent)


@pytest.mark.parametrize("impl", [
    change_making, change_making_support_d1_absent,
])
def test_change_making(impl: Callable[[Sequence[int], int], int | None]):
    assert impl([1], 0) == 0
    assert impl([1], 1) == 1
    assert impl([1], 2) == 2

    assert impl([1, 2], 0) == 0
    assert impl([1, 2], 1) == 1
    assert impl([1, 2], 2) == 1
    assert impl([1, 2], 3) == 2
    assert impl([1, 2], 4) == 2

    # test case/example in the book
    assert impl([1, 3, 4], 6) == 2
    assert impl([1, 3, 4], 5) == 2
    assert impl([1, 3, 4], 4) == 1
    assert impl([1, 3, 4], 3) == 1
    assert impl([1, 3, 4], 2) == 2
    assert impl([1, 3, 4], 1) == 1
    assert impl([1, 3, 4], 0) == 0


def test_change_making_support_d1_absent():
    assert change_making_support_d1_absent([3, 5], 2) is None
    assert change_making_support_d1_absent([3, 5], 7) is None

    assert change_making_support_d1_absent([3, 5], 6) == 2
    assert change_making_support_d1_absent([3, 5], 8) == 2
    assert change_making_support_d1_absent([3, 5], 9) == 3
