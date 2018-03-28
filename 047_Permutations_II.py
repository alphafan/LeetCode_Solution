"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.permuteUniqueRec(nums, [], [False]*len(nums))

    def permuteUniqueRec(self, nums, partial, used):
        if len(nums) == 0:
            print(partial)
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            self.permuteUniqueRec(nums, partial+nums[i], used)
            used[i] = False

