from dynamic_programming_study.coin_row import coin_row_conventional


def test_coin_row_conventional():
    assert coin_row_conventional(()) == 0
    assert coin_row_conventional([]) == 0

    assert coin_row_conventional((1,)) == 1
    assert coin_row_conventional([42]) == 42

    assert coin_row_conventional([1, 2]) == 2
    assert coin_row_conventional([2, 1]) == 2

    assert coin_row_conventional([1, 2, 3]) == 4
    assert coin_row_conventional([1, 10, 3]) == 10

    assert coin_row_conventional([1, 2, 3, 10]) == 12
    assert coin_row_conventional([1, 1, 3, 1]) == 4
