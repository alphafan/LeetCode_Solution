"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""

import random


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        landPoints = []
        nRow, nCol = len(grid), len(grid[0])
        for row in range(nRow):
            for col in range(nCol):
                if grid[row][col] == 1:
                    landPoints.append([row, col])
        numIsland = 0
        while len(landPoints):
            startPoint = landPoints[-1]
            islandPoints, visited = [startPoint], []
            numIsland += 1
            # A breadth first search to find island
            while islandPoints:
                point = islandPoints.pop(0)
                if point not in visited:
                    visited.append(point)
                    connectedPoints = [
                        [point[0], point[1] + 1],
                        [point[0], point[1] - 1],
                        [point[0] + 1, point[1]],
                        [point[0] - 1, point[1]],
                    ]
                    for row, col in connectedPoints:
                        if 0 <= row < nRow and 0 <= col < nCol and \
                                grid[row][col] == 1 and \
                                [row, col] not in visited:
                            islandPoints.append([row, col])
            for point in visited:
                landPoints.remove(point)
        return numIsland


grid = []
for i in range(5):
    row = [random.randint(0, 1) for _ in range(5)]
    grid.append(row)
    print(row)
s = Solution()
r = s.numIslands(grid)
print(r)









