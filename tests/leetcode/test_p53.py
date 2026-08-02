from leetcode.p53 import max_sub_array_sum


def test_max_sub_array_sum():
    assert max_sub_array_sum([]) == 0

    assert max_sub_array_sum([-1]) == 0
    assert max_sub_array_sum([-1, -2]) == 0

    assert max_sub_array_sum([1]) == 1
    assert max_sub_array_sum([5, 4, -1, 7, 8]) == 23
    assert max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    assert max_sub_array_sum([-1]) == 0
    assert max_sub_array_sum([-1, -3]) == 0
