"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        maxLength = 0
        for num in numsSet:
            if num-1 not in numsSet:
                currLength = 1
                n = num
                while n+1 in numsSet:
                    n = n+1
                    currLength += 1
                maxLength = max(maxLength, currLength)
        return maxLength
