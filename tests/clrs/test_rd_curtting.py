from collections.abc import Callable

import pytest

from clrs.rod_cutting import cut_rod, cut_rod_price_seeded


@pytest.mark.parametrize("impl", [cut_rod, cut_rod_price_seeded])
def test_cut_rod(impl: Callable[[list[int]], int]):
    assert impl([0]) == 0
    assert impl([0, 1]) == 1
    assert impl([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]) == 30
    assert impl([0, 1, 5, 8, 9]) == 10
    assert impl([0, 1, 5, 8, 9, 10, 17, 17]) == 18


@pytest.mark.parametrize("impl", [cut_rod, cut_rod_price_seeded])
@pytest.mark.parametrize("prices, ex", [
    ([], IndexError),  # prices[0] on empty list
    ([1], AssertionError),  # prices[0] must be 0
])
def test_cut_rod_invalid_prices(
        impl: Callable[[list[int]], int], prices: list[int], ex):
    with pytest.raises(ex):
        impl(prices)
