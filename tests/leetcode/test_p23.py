from collections.abc import Callable

import pytest

from leetcode.p23 import (ListNode, merge_k_sorted_linked_lists,
                          merge_k_sorted_lists, merge_k_sorted_lists_2)


def test_merge_k_sorted_linked_lists():
    assert merge_k_sorted_linked_lists(cc([])) == c([])
    assert merge_k_sorted_linked_lists(cc([[]])) == c([])
    assert merge_k_sorted_linked_lists(cc([[], []])) == c([])

    assert merge_k_sorted_linked_lists(cc([[1, 3]])) == c([1, 3])
    assert merge_k_sorted_linked_lists(cc([[1, 3], []])) == c([1, 3])
    assert merge_k_sorted_linked_lists(cc([[], [1, 3]])) == c([1, 3])

    assert merge_k_sorted_linked_lists(cc([[2, 4], [1, 3]])) == c([1, 2, 3, 4])

    assert merge_k_sorted_linked_lists(cc([
        [1, 4, 5], [1, 3, 4], [2, 6]
    ])) == c([1, 1, 2, 3, 4, 4, 5, 6])


def c(lst: list[int]) -> ListNode | None:
    ret: ListNode | None = None
    for x in reversed(lst):
        ret = ListNode(x, ret)
    return ret


def cc(lists: list[list[int]]) -> list[ListNode | None]:
    return [c(lst) for lst in lists]


@pytest.mark.parametrize("impl", [
    merge_k_sorted_lists, merge_k_sorted_lists_2])
def test_merge_k_sorted_lists(impl: Callable[[list[list[int]]], list[int]]):
    assert impl([]) == []
    assert impl([[]]) == []
    assert impl([[], []]) == []

    assert impl([[1, 3]]) == [1, 3]
    assert impl([[1, 3], []]) == [1, 3]
    assert impl([[], [1, 3]]) == [1, 3]

    assert impl([[2, 4], [1, 3]]) == [1, 2, 3, 4]

    assert impl([
        [1, 4, 5], [1, 3, 4], [2, 6]
    ]) == [1, 1, 2, 3, 4, 4, 5, 6]
