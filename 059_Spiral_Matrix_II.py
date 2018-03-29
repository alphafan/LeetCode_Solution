"""

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        rowStart, rowEnd, colStart, colEnd = 0, n-1, 0, n-1
        matrix = [[0]*n for _ in range(n)]
        num = 0
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd+1):
                num += 1
                matrix[rowStart][i] = num
            rowStart += 1
            for i in range(rowStart, rowEnd+1):
                num += 1
                matrix[i][colEnd] = num
            colEnd -= 1
            for i in range(colEnd, colStart-1, -1):
                num += 1
                matrix[rowEnd][i] = num
            rowEnd -= 1
            for i in range(rowEnd, rowStart-1, -1):
                num += 1
                matrix[i][colStart] = num
            colStart += 1
        return matrix


s = Solution()
r = s.generateMatrix(5)
print(r)