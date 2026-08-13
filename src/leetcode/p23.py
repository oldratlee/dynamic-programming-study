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
from __future__ import annotations

import heapq
from dataclasses import dataclass


def merge_k_sorted_linked_lists(lists: list[LinkedList[int]]) \
        -> LinkedList[int]:
    """
    Merge k sorted singly-linked lists into one sorted list using a min-heap.

    Algorithm (k-way merge via heap):
      1. Seed the heap with the head node of every non-empty input list.
      2. Repeatedly pop the smallest head from the heap and append it to
         the result chain.
      3. After popping a node, advance its source list by one and push the
         next node back into the heap (if one exists).
      4. When the heap is drained, every node from every input list has been
         placed in ascending order.

    Time : O(N log k)  — N total nodes, k lists; each push/pop is O(log k).
    Space: O(k)       — the heap never holds more than one node per list.
    """
    heap_list = [_ListNodeElementInHeap(lst.val, idx, lst)
                 for idx, lst in enumerate(lists) if lst]
    # Turn the list into a min-heap in O(k)
    heapq.heapify(heap_list)

    # `dummy_head` is a sentinel whose `next` points to the real first node;
    #     it simplifies head-insertion logic (no special "first node" case).
    # `tail` always refers to the last node already linked into the result.
    dummy_head = tail = ListNode(0)

    while heap_list:
        # Pop the globally smallest current head
        #   among all active lists in O(log k)
        ele = heapq.heappop(heap_list)
        # Append to the result Linked List
        #
        # Chained assignment `a = b = expr` evaluates `expr` ONCE,
        #   then assigns to targets left-to-right.
        # Here `tail.next` MUST be set BEFORE `tail` is rebound,
        #   otherwise the old tail's `next` would never be linked.
        # do NOT swap assignment targets to `tail = tail.next = ...`
        tail.next = tail = ListNode(ele.head)

        # If the list this element came from still has more nodes,
        # forward one element and put it back in the heap.
        #
        # `nxt` is the next node in that source list (or None).
        if nxt := ele.lst.next:
            # Update sort key & payload node
            ele.head, ele.lst = nxt.val, nxt
            # Re-insert; heap re-sorts in O(log k)
            heapq.heappush(heap_list, ele)

    return dummy_head.next


@dataclass
class ListNode[T]:
    """
    singly-linked list node
    """
    val: T
    next: LinkedList[T] = None


type LinkedList[T] = ListNode[T] | None


def reverse_linked_list[T](lst: LinkedList[T]) -> LinkedList[T]:
    reversed_list: LinkedList[T] = None
    while lst:
        reversed_list = ListNode(lst.val, reversed_list)
        lst = lst.next
    return reversed_list


@dataclass(order=True)
class _ListNodeElementInHeap[T]:
    # Unique heap ordering key:
    #  - current head value
    #  - List index in input; tie-breaker so equal heads stay stably ordered
    head: T
    list_index_in_input: int
    # Payload (not part of the ordering key)
    lst: ListNode[T]


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
