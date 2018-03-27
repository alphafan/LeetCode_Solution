"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchRec(nums, target, 0, len(nums) - 1)

    def searchRec(self, nums, target, start, end):
        if start <= end:
            mid = int((start+end)/2)
            if nums[mid] == target:
                return mid
            # start     5
            # mid       2
            # end       3
            # target    6
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    return self.searchRec(nums, target, start, mid-1)
                else:
                    return self.searchRec(nums, target, mid+1, end)
            else:
                if nums[mid] < target <= nums[end]:
                    return self.searchRec(nums, target, mid+1, end)
                else:
                    return self.searchRec(nums, target, start, mid-1)
        else:
            return -1

s = Solution()
n = [5, 1, 3]
r = s.search(n, 3)
print(r)