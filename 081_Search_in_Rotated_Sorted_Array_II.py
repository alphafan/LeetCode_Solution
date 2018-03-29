"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums)-1
        while start < end:
            mid = int((start+end)/2)
            if nums[mid] == target:
                res = [mid]
                for i in range(mid+1, end+1):
                    if nums[i] == target:
                        res.append(i)
                    else:
                        break
                for i in range(mid-1, start-1, -1):
                    if nums[i] == target:
                        res.append(i)
                    else:
                        break
                return res
            if nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


n = [4, 5, 6, 7, 0, 0, 0, 0, 1, 2, 2, 2]
s = Solution()
r = s.search(n, 4)
print(r)