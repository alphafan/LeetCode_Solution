"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""

import sys


class Solution(object):
    """ Some bugs inside ... """

    memo = {}

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memo = {}
        if len(nums) == 0 or len(nums) == 1:
            return 0
        return self.jumpRec(nums, 0, 0)

    def jumpRec(self, nums, currentIndex, step):
        if (currentIndex, step) in self.memo:
            return self.memo[(currentIndex, step)]
        canJump = nums[currentIndex]
        if currentIndex + canJump >= len(nums)-1:
            self.memo[(currentIndex, step)] = step + 1
            return step + 1
        if canJump != 0:
            res = min([self.jumpRec(nums, currentIndex + i, step + 1)
                       for i in range(1, canJump+1)])
            self.memo[(currentIndex, step)] = res
            return res
        else:
            self.memo[(currentIndex, step)] = sys.maxsize
            return sys.maxsize


s = Solution()
a = [2,3,1,1,4]
print(s.jump(a))
