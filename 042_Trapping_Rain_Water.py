"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!
"""


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for i, in range(len(height)):
            maxLeftHeight = max(height[:i+1])
            maxRightHeight = max(height[i:])
            res += min(maxLeftHeight, maxRightHeight) - height[i]
        return res

    def trap2(self, height):
        maxLeftHeight = [height[0]] + [0] * (len(height)-1)
        maxRightHeight = [0] * (len(height)-1) + [height[-1]]
        for i in range(len(height)-1):
            if height[i+1] > maxLeftHeight[i]:
                maxLeftHeight[i+1] = height[i+1]
            else:
                maxLeftHeight[i+1] = maxLeftHeight[i]
        print(maxLeftHeight)
        for j in range(len(height)-1, 0, -1):
            if height[j-1] > maxRightHeight[j]:
                maxRightHeight[j-1] = height[j-1]
            else:
                maxRightHeight[j-1] = maxRightHeight[j]
        print(maxRightHeight)
        res = 0
        for lmax, rmax, h in zip(maxLeftHeight, maxRightHeight, height):
            res += min(lmax, rmax) - h
        return res

    def trap3(self, height):
        res, left, right = 0, 0, len(height)-1
        leftMax, rightMax = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                res += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                res += rightMax - height[right]
                right -= 1
        return res


h = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap3(h))
