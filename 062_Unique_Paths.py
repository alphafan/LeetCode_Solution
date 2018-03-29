"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""


class Solution(object):

    memo = {}

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        if m == 1 or n == 1:
            self.memo[(m, n)] = 1
            return 1
        res = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        self.memo[(m, n)] = res
        return res


s = Solution()
print(s.uniquePaths(100, 100))
