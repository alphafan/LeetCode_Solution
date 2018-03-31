"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""


class Solution(object):

    memo = {}

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # If I'm at triangle[i][j]
        # next step I can choose from triangle[i+1][j] or triangle[i+1][j+1]
        if len(triangle) == 0:
            return 0
        return self.minimumTotalHelper(triangle, 0, 0, len(triangle), 0)

    def minimumTotalHelper(self, triangle, rowIndex, colIndex, height, currSum):
        if (rowIndex, colIndex, currSum) in self.memo:
            return self.memo[(rowIndex, colIndex, currSum)]
        currSum += triangle[rowIndex][colIndex]
        if rowIndex == height - 1:
            self.memo[(rowIndex, colIndex, currSum)] = currSum
            return currSum
        f = self.minimumTotalHelper
        res1 = f(triangle, rowIndex+1, colIndex, height, currSum)
        res2 = f(triangle, rowIndex+1, colIndex+1, height, currSum)
        self.memo[(rowIndex, colIndex, currSum)] = min(res1, res2)
        return min(res1, res2)

s = Solution()
t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
r = s.minimumTotal(t)
print(r)
