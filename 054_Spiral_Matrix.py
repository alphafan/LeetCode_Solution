"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):

    def spiralOrder(self, matrix, row, col):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if row == 0 or col == 0:
            return []
        elif row == 1:
            return matrix[0]
        elif col == 1:
            return [row[0] for row in matrix]
        else:
            res = matrix[0]
            for i in range(1, row-1):
                res += [matrix[i][-1]]
            res += matrix[-1][::-1]
            for i in range(row-2, 0, -1):
                res += [matrix[i][0]]
            remain = matrix[1:row-1]
            remain = [row[1:len(row)-1] for row in remain]
            return res + self.spiralOrder(remain, row-2, col-2)


s = Solution()
m = [
 [ 1, 2, 3, 4, 5 ],
 [ 4, 5, 6, 7, 3 ],
 [ 7, 8, 9, 10, 2],
 [ 4, 6, 7, 1, 1]
]
print(s.spiralOrder(m, 4, 5))
# print(*(zip([[0], [1]])))
