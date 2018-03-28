"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3, --> lower: 2, upper: 2
and [3,4,-1,1] return 2. --> lower: 1, upper: 3

nums:   1 5 4 2 3 6 8
lower:  1 1 1 2 3
upper:  1 5 4 4

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Idea:
        1. For any array whose length is l, the first missing positive value
            must in 1, 2, 3, ..., l+1, so we only care about the values in this
            range and remove the rest
        2. We can use the array index as the hash to restore the frequency
            of each number within the range 1, 2, 3, ..., l
        """
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i]%n] += n
        for i in range(1, n):
            if int(nums[i]/n) == 0:
                return i
        return n
