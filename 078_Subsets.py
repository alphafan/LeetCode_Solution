"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = [[]]
        for i, num in enumerate(nums):
            expandRes = [r+[num] for r in res]
            res = res + expandRes
        res.sort()
        return res

s = Solution()
r = s.subsets([1, 2, 3])
print(r)
