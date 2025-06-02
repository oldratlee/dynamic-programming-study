from dp_study.idaa3e.ch8_1_example3_coin_collecting import collect_coin


def test_collect_coin():
    assert collect_coin([]) == 0
    assert collect_coin([[]]) == 0
    assert collect_coin([[], []]) == 0
    # test case/example in the book
    assert collect_coin([
        [False, False, False, False, True, False],
        [False, True, False, True, False, False],
        [False, False, False, True, False, True],
        [False, False, True, False, False, True],
        [True, False, False, False, True, False]
    ]) == 5
