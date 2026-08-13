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


def max_sub_array_sum(nums: Sequence[int]) -> int:
    # Kadane's algorithm — single-pass O(n) dynamic programming approach.
    #
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
        max_sum = max(cur_sum, max_sum)
    return max_sum
