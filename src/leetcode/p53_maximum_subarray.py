"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray

Given an integer array `nums`, find the subarray with the largest sum,
and return _its sum_.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
* `1 <= nums.length <= 10e5`
* `-104 <= nums[i] <= 10e4`

**Follow up:** If you have figured out the `O(n)` solution,
               try coding another solution using
               the **divide and conquer** approach, which is more subtle.
"""

from collections.abc import Sequence
from itertools import islice


def max_subarray_sum_kadane(nums: Sequence[int]) -> int:
    """
    Largest sum of any contiguous subarray, with the *empty* subarray allowed.
    Uses Kadane's algorithm — a single-pass O(n) dynamic programming approach.

    Unlike the non-empty variant, `cur_sum = max_sum = 0` lets the running sum
    restart from the empty subarray, so an all-negative input returns 0
    (the empty subarray's sum) instead of the least-negative single element.

    Time : O(n)  — one pass over the array.
    Space: O(1)  — only two scalar accumulators.
    """
    # cur_sum: running sum of *the best subarray ending at the current index*.
    #          At each step we decide whether to extend the previous subarray
    #          (cur_sum + num) or start fresh from the current element (num).
    #          Taking the max of the two is the DP recurrence.
    #
    # max_sum: global best subarray sum seen so far across all indices.
    #          Updated after every step so it always reflects the answer.
    cur_sum = max_sum = 0
    for num in nums:
        # Either grow the existing subarray by `num`, or restart a new
        # subarray at `num`. Restarting wins when the prior running sum
        # is negative (it would only drag the total down).
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


def max_subarray_sum_accumulate(nums: Sequence[int]) -> int:
    """
    Largest sum of any contiguous subarray, with the *empty* subarray allowed.
    Enumerates every subarray in O(n^2) by extending a running sum.

    For each `start`, `cur_sum` is the sum of `nums[start:end + 1]`.
    Extending `end` by one is O(1) (`cur_sum += nums[end]`), so all O(n^2)
    subarrays are considered without re-summing from scratch (which would
    be the O(n^3) brute-force approach).

    `max_sum = 0` seeds the answer with the empty subarray's sum, so an
    all-negative input returns 0 instead of the least-negative single element.

    Time : O(n^2) — nested loops over start and end indices.
    Space: O(1)   — only two scalar accumulators.
    """
    max_sum = 0
    # Enumerate every non-empty subarray `nums[start:end + 1]`.
    #   start: inclusive left index (0 .. len(nums) - 1).
    #   end:   inclusive right index, running from `start` (single element)
    #          up to `len(nums) - 1` (rest of the array).
    for start in range(len(nums)):
        # Reset the running sum for a new left endpoint.
        # Each inner-loop step then grows the same subarray by one element.
        cur_sum = 0
        for end in range(start, len(nums)):
            cur_sum += nums[end]
            max_sum = max(max_sum, cur_sum)
    return max_sum


def max_subarray_sum_brute_force(nums: Sequence[int]) -> int:
    """
    Largest subarray sum by enumerating every subarray (brute force),
    with the *empty* subarray allowed.

    `max_sum = 0` seeds the answer with the empty subarray's sum, so an
    all-negative input returns 0 instead of the least-negative single element.

    Time : O(n^3) — O(n^2) subarrays, each summed over its length.
    Space: O(1)   — `islice` is lazy; no subarray slice is allocated.
    """
    max_sum = 0
    # Enumerate every non-empty subarray `nums[start:stop]`.
    #   start: inclusive left index of the subarray. It visits every possible
    #      starting position in the array (0 .. len(nums) - 1).
    #   stop:  exclusive right index (one past the last element), running from
    #      `start + 1` (single element) up to `len(nums)` (rest of the array).
    for start in range(len(nums)):
        for stop in range(start + 1, len(nums) + 1):
            # Use `islice(nums, start, stop)` instead of `nums[start:stop]`
            #   to sum the subarray without allocating an intermediate list.
            # Slicing would copy O(length) elements per subarray;
            #   the lazy iterator keeps the extra space O(1).
            max_sum = max(max_sum, sum(islice(nums, start, stop)))
    return max_sum


def max_nonempty_subarray_sum_kadane(nums: Sequence[int]) -> int | None:
    """
    Largest sum of any non-empty subarray via Kadane's algorithm.

    Returns `None` for an empty input.

    Time : O(n)  — one pass over the array.
    Space: O(1)  — only two scalar accumulators.
    """
    if not nums:
        return None

    cur_sum = max_sum = nums[0]
    # Use `islice(nums, 1, None)` instead of `nums[1:]`
    #   to skip the first element without allocating a new list.
    # For large inputs this avoids an O(n) copy,
    #   keeping the loop O(n) time and O(1) extra space.
    for num in islice(nums, 1, None):
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


def max_nonempty_subarray_sum_accumulate(nums: Sequence[int]) -> int | None:
    """
    Largest sum of any non-empty subarray by enumerating every subarray
    with a running sum.

    For each `start`, `cur_sum` is the sum of `nums[start:end + 1]`.
    Extending `end` by one is O(1) (`cur_sum += nums[end]`), so all O(n^2)
    non-empty subarrays are considered without re-summing from scratch
    (which would be the O(n^3) brute-force approach).

    Returns `None` for an empty input. `max_sum = nums[0]` seeds the answer
    with a real element, so an all-negative input returns the largest
    (least-negative) single element rather than 0.

    Time : O(n^2) — nested loops over start and end indices.
    Space: O(1)   — only two scalar accumulators.
    """
    if not nums:
        return None

    max_sum = nums[0]
    # Enumerate every non-empty subarray `nums[start:end + 1]`.
    #   start: inclusive left index (0 .. len(nums) - 1).
    #   end:   inclusive right index, running from `start` (single element)
    #          up to `len(nums) - 1` (rest of the array).
    for start in range(len(nums)):
        # Reset the running sum for a new left endpoint.
        # Each inner-loop step then grows the same subarray by one element.
        cur_sum = 0
        for end in range(start, len(nums)):
            cur_sum += nums[end]
            max_sum = max(max_sum, cur_sum)
    return max_sum


def max_nonempty_subarray_sum_brute_force(nums: Sequence[int]) -> int | None:
    """
    Largest sum of any non-empty subarray by enumerating every subarray.

    Returns `None` for an empty input.

    Time : O(n^3) — O(n^2) subarrays,
                    each summed over its length (slicing + sum).
    Space: O(n)   — the temporary slice `nums[start:stop]`
                    holds up to n elements.
    """
    if not nums:
        return None

    max_sum = nums[0]
    # Enumerate every non-empty subarray `nums[start:stop]`.
    for start in range(len(nums)):
        for stop in range(start + 1, len(nums) + 1):
            max_sum = max(max_sum, sum(nums[start:stop]))
    return max_sum
