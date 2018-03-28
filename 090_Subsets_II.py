"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        i, res = 0, [[]]
        while i < len(nums):
            dup = 0
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                dup += 1
                i += 1
            if dup:
                before = res
                for d in range(1, dup+2):
                    expandRes = [r + [nums[i]] * d for r in before]
                    res = res + expandRes
            else:
                expandRes = [r+[nums[i]] for r in res]
                res = res + expandRes
            i += 1
        res.sort()
        return res

s = Solution()
r = s.subsetsWithDup([1, 1])
print(r)