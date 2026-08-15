from leetcode.p53 import max_nonempty_subarray_sum, max_subarray_sum


def test_max_subarray_sum():
    assert max_subarray_sum([]) == 0

    assert max_subarray_sum([-1]) == 0
    assert max_subarray_sum([-1, -2]) == 0
    assert max_subarray_sum([-3, -1, -2]) == 0

    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_nonempty_subarray_sum():
    assert max_nonempty_subarray_sum([]) is None

    assert max_nonempty_subarray_sum([-1]) == -1
    assert max_nonempty_subarray_sum([-1, -2]) == -1
    assert max_nonempty_subarray_sum([-3, -1, -2]) == -1

    assert max_nonempty_subarray_sum([1]) == 1
    assert max_nonempty_subarray_sum([5, 4, -1, 7, 8]) == 23
    assert max_nonempty_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
