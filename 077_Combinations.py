"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        nums = list(range(1, n+1))
        return self.combineRec(nums, k)

    def combineRec(self, nums, k):
        if k == 1:
            return [[num] for num in nums]
        else:
            res = []
            for i, num in enumerate(nums):
                remain = nums[i+1:]
                for r in self.combineRec(remain, k-1):
                    res.append([num]+r)
            return res


s = Solution()
r = s.combine(3, 2)
print(r)