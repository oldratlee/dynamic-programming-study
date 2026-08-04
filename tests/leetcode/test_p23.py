from leetcode.p23 import merge_k_sorted_lists


def test_merge_k_sorted_lists():
    assert merge_k_sorted_lists([]) == []
    assert merge_k_sorted_lists([[]]) == []
    assert merge_k_sorted_lists([[], []]) == []

    assert merge_k_sorted_lists([[1, 3]]) == [1, 3]
    assert merge_k_sorted_lists([[1, 3], []]) == [1, 3]
    assert merge_k_sorted_lists([[], [1, 3]]) == [1, 3]

    assert merge_k_sorted_lists([[2, 4], [1, 3]]) == [1, 2, 3, 4]

    assert merge_k_sorted_lists([
        [1, 4, 5], [1, 3, 4], [2, 6]
    ]) == [1, 1, 2, 3, 4, 4, 5, 6]
