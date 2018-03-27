"""
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order
(ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
1,4,3 -> 3,1,4
1,2,3 -> 1,3,2
1,3,2 -> 2,1,3
1,2,4,3 -> 1,3,2,4
4,1,2,3 -> 4,1,3,4
1,2,5,4,3 -> 1,3,2,4,5
"""


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums -> left and right
        # If right is in descending order
        # most right item of left part increase, right part turn increasing order
        # Step 1: Get the split index
        i = len(nums)-1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        if i == 0:
            nums = self.reverse(nums)
            return nums
        splitIndex = i-1
        print(nums)
        print(splitIndex)
        # left is nums[:splitIndex], right is nums[splitIndex:]
        numLargerThanSplit, diff = nums[splitIndex], 99999
        numLargerThanSplitIndex = splitIndex
        for i, num in enumerate(nums[splitIndex+1:]):
            if num > nums[splitIndex]:
                if num - nums[splitIndex] < diff:
                    diff = num-nums[splitIndex]
                    numLargerThanSplitIndex = i+splitIndex+1
        print(numLargerThanSplitIndex)
        nums[splitIndex], nums[numLargerThanSplitIndex] = nums[numLargerThanSplitIndex], nums[splitIndex]
        nums[splitIndex+1:] = sorted(nums[splitIndex+1:])
        return nums

    def reverse(self, nums):
        for i in range(int(len(nums)/2)):
            nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
        return nums

s = Solution()
nums = [3,2,1]
print(s.nextPermutation(nums))
