"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists

You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
* k == lists.length
* 0 <= k <= 104
* 0 <= lists[i].length <= 500
* -104 <= lists[i][j] <= 104
* lists[i] is sorted in ascending order.
* The sum of lists[i].length will not exceed 104.
"""
import heapq
from dataclasses import dataclass


def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    heap_list = [_ElementInHeap(lst[0], idx, lst, 0)
                 for idx, lst in enumerate(lists) if lst]
    heapq.heapify(heap_list)

    ret: list[int] = []
    while heap_list:
        ele = heapq.heappop(heap_list)
        ret.append(ele.head)

        ele.head_index += 1
        if ele.head_index == len(ele.lst):
            continue
        ele.head = ele.lst[ele.head_index]
        heapq.heappush(heap_list, ele)

    return ret


@dataclass(order=True)
class _ElementInHeap:
    # Unique heap ordering key:
    #  - current head value
    #  - List index in input; tie-breaker so equal heads stay stably ordered
    head: int
    list_index_in_input: int
    # Payload (not part of the ordering key)
    lst: list[int]
    head_index: int


def merge_k_sorted_lists_2(lists: list[list[int]]) -> list[int]:
    sorted_lists: list[tuple[list[int], int]] = sorted(
        ((l, idx) for idx, l in enumerate(lists) if l),
        key=lambda x: (x[0][0], x[1])
    )
    list_count = len(sorted_lists)

    def reorder(idx: int):
        me: tuple[list[int], int] = sorted_lists[idx]
        assert me
        me_key = (me[0][0], me[1])

        start, end = idx, list_count
        while end - start > 1:
            target = (start + end) // 2
            if me_key <= (sorted_lists[target][0][0], sorted_lists[target][1]):
                end = target
            else:
                start = target

        if start == idx:
            return
        sorted_lists.insert(start, sorted_lists.pop(idx))

    ret: list[int] = []
    i = 0
    while i < list_count:
        while True:
            ret.append(sorted_lists[i][0][0])
            del sorted_lists[i][0][0]
            if not sorted_lists[i][0]:
                i += 1
                break
            reorder(i)

    return ret
