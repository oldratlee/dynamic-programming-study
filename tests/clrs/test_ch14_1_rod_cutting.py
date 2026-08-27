from collections.abc import Callable

import pytest

from clrs.ch14_1_rod_cutting import (cut_rod_first_cut,
                                     cut_rod_first_cut_1indexed, cut_rod_split,
                                     cut_rod_split_seeded)


@pytest.mark.parametrize("impl", [
    cut_rod_split, cut_rod_split_seeded,
    cut_rod_first_cut, cut_rod_first_cut_1indexed])
def test_cut_rod(impl: Callable[[list[int]], int]):
    assert impl([]) == 0
    assert impl([1]) == 1
    assert impl([1, 5, 8, 9, 10, 17, 17, 20, 24, 30]) == 30
    assert impl([1, 5, 8, 9]) == 10
    assert impl([1, 5, 8, 9, 10, 17, 17]) == 18
