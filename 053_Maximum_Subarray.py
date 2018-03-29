"""
Find the contiguous sub array within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous sub array [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):

    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum+num)
            maxSum = max(currSum, maxSum)
        return maxSum

s = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
r = s.maxSubArray(a)
print(r)
