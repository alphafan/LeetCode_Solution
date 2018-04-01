"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

class Solution(object):

    def findMin(self, nums):
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums)-1
        while start <= end:
            mid = int((start+end)/2)
            if start == end or (mid > 0 and nums[mid] < nums[mid-1]):
                return nums[mid]
            #                    s    m    e
            # 5, 1, 2, 3, 4 -->  5    2    4 --> s - m
            # 4, 5, 1, 2, 3 -->  4    1    3 -->
            # 3, 4, 5, 1, 2 -->  3    5    2 --> m - e  ?? nums[mid] > nums[end]
            # 2, 3, 4, 5, 1 -->  2    3    1 --> m - e
            # 1, 2, 3, 4, 5 -->  1    3    5 --> s - m
            if nums[end] > nums[start]:
                # This array is in ascending order
                # Return first item
                return nums[start]
            if nums[mid] < nums[end] <= nums[start]:
                # 5, 1, 2, 3, 4
                end = mid - 1
                # Deal with duplicate:
                while end > start and nums[end-1] == nums[end]:
                    end -= 1
            elif nums[end] <= nums[start] <= nums[mid]:
                # 2, 3, 4, 5, 1
                start = mid + 1
                while start < end and nums[start] == nums[start+1]:
                    start += 1


s = Solution()
n = [1, 1, 0, 1]
print(s.findMin(n))
