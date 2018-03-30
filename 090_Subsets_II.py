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

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = set()
        nums.sort()
        self.subsetHelper(nums, 0, [], results)
        return results

    def subsetHelper(self, nums, index, partial, results):
        if index == len(nums):
            results.add(tuple(partial))
            return
        self.subsetHelper(nums, index+1, partial+[nums[index]], results)
        self.subsetHelper(nums, index+1, partial, results)

s = Solution()
r = s.subsets([1, 2, 2])
print(r)