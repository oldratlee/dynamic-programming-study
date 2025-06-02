from collections.abc import Callable, Sequence

import pytest

from dp_study.idaa3e.ch8_1_example2_change_making import (
    make_change, make_change_support_d1_absent)


@pytest.mark.parametrize("impl", [
    make_change, make_change_support_d1_absent])
@pytest.mark.parametrize("args, expected", [
    [([1], 0), 0],
    [([1], 1), 1],
    [([1], 2), 2],
    [([1, 2], 0), 0],
    [([1, 2], 1), 1],
    [([1, 2], 2), 1],
    [([1, 2], 3), 2],
    [([1, 2], 4), 2],

    # test case/example in the book
    [([1, 3, 4], 6), 2],
    [([1, 3, 4], 5), 2],
    [([1, 3, 4], 4), 1],
    [([1, 3, 4], 3), 1],
    [([1, 3, 4], 2), 2],
    [([1, 3, 4], 1), 1],
    [([1, 3, 4], 0), 0],
])
def test_make_change(impl: Callable[[Sequence[int], int], int | None],
                     args, expected: int):
    assert impl(*args) == expected


def test_make_change_support_d1_absent():
    assert make_change_support_d1_absent([3, 5], 2) is None
    assert make_change_support_d1_absent([3, 5], 7) is None

    assert make_change_support_d1_absent([3, 5], 6) == 2
    assert make_change_support_d1_absent([3, 5], 8) == 2
    assert make_change_support_d1_absent([3, 5], 9) == 3
