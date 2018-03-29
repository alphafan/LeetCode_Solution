"""
Given a m x n grid filled with non-negative numbers, find a path from top
left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):

    """ Add DP to fatser """

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [[]]:
            return 0
        return self.minPathSumRec(grid, 0, 0, len(grid), len(grid[0]), 0)

    def minPathSumRec(self, grid, row, col, nRows, nCols, pathSum):
        if row == nRows-1 and col == nCols-1:
            return pathSum + grid[row][col]
        elif row == nRows-1:
            return self.minPathSumRec(grid, row, col+1, nRows, nCols, pathSum + grid[row][col])
        elif col == nCols-1:
            return self.minPathSumRec(grid, row+1, col, nRows, nCols, pathSum + grid[row][col])
        else:
            return min(
                self.minPathSumRec(grid, row, col + 1, nRows, nCols, pathSum + grid[row][col]),
                self.minPathSumRec(grid, row + 1, col, nRows, nCols, pathSum + grid[row][col])
            )


s = Solution()
g = [[1]]
print(s.minPathSum(g))
