"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permuteRec(nums, [])

    def permuteRec(self, nums, partial):
        if len(nums) == 0:
            print(partial)
        else:
            for i, num in enumerate(nums):
                remain = nums[:i] + nums[i+1:]
                self.permuteRec(remain, partial+[num])


s = Solution()
n = [1, 2, 3, 4]
s.permute(n)
