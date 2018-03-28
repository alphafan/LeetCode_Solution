"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):

    def combinationSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        def findRec(nums, target, partial):
            current = sum(partial)
            if current == target:
                print('Sum({})={}'.format(partial, target))
            elif current < target:
                for i, num in enumerate(nums):
                    # Can be duplicate
                    findRec(nums[i:], target, partial+[num])
                    # Can not be duplicate
                    # findRec(nums[i+1:], target, partial + [num])

        findRec(nums, target, results)
        return results


s = Solution()
nums = [2, 3, 6, 7]
target = 7
r = s.combinationSum(nums, target)
print(r)
