from dynamic_programming_study.change_making import change_making


def test_change_making():
    assert change_making([1], 0) == 0
    assert change_making([1], 1) == 1
    assert change_making([1], 2) == 2

    assert change_making([1, 2], 0) == 0
    assert change_making([1, 2], 1) == 1
    assert change_making([1, 2], 2) == 1
    assert change_making([1, 2], 3) == 2
    assert change_making([1, 2], 4) == 2

    # test case/example in the book
    assert change_making([1, 3, 4], 6) == 2
    assert change_making([1, 3, 4], 5) == 2
    assert change_making([1, 3, 4], 4) == 1
    assert change_making([1, 3, 4], 3) == 1
    assert change_making([1, 3, 4], 2) == 2
    assert change_making([1, 3, 4], 1) == 1
    assert change_making([1, 3, 4], 0) == 0
