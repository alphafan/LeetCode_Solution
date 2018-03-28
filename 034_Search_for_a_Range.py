"""
Given an array of integers sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                lrange, rrange = mid, mid
                while lrange > 0 and nums[lrange-1] == target:
                    lrange -= 1
                while rrange < len(nums)-1 and nums[rrange+1] == target:
                    rrange += 1
                return [lrange, rrange]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]

s = Solution()
test = [5, 5, 6]
r = s.searchRange(test, 8)
print(r)
