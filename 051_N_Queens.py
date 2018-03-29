"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):

    def __init__(self):
        self.colForRow = None
        self.solutions = 0

    def solve(self, n):
        self.colForRow = [None] * n
        self.place(0, n)
        print(self.solutions)

    def place(self, row, n):
        if row == n:
            print(self.colForRow)
            self.solutions += 1
            return
        for i in range(n):
            self.colForRow[row] = i
            if self.check(row):
                self.place(row+1, n)

    def check(self, row):
        for i in range(row):
            if self.colForRow[i] is not None and self.colForRow[row] is not None:
                diff = self.colForRow[i] - self.colForRow[row]
                if diff == 0 or abs(diff) == abs(row-i):
                    return False
        return True


s = Solution()
s.solve(5)
