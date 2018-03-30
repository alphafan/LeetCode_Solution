"""
Given n non-negative integers representing the histogram's bar height
where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""

import sys


class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        minValueIndex, minValue = sys.maxsize, sys.maxsize
        for i, value in enumerate(heights):
            if value < minValue:
                minValue = value
                minValueIndex = i
        return max(minValue*len(heights),
                   self.largestRectangleArea(heights[:minValueIndex]),
                   self.largestRectangleArea(heights[minValueIndex+1:]))


s = Solution()
heights = [2,1,5,6,2,3]
r = s.largestRectangleArea(heights)
print(r)
