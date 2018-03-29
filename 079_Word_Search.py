"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

import copy


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 1) Search the position of first character -->
        #       list of [i, j] positions and next search region
        # 2) Check search region to see if match the second char
        # 3) Update search region and continue search next char util there is no more char
        if len(board) == 0 or len(board[0]) == 0:
            return False
        if len(word) == 0:
            return True
        nRow, nCol = len(board), len(board[0])
        for i in range(nRow):
            for j in range(nCol):
                if board[i][j] == word[0]:
                    searchRegion = set()
                    for row in range(i - 1, i + 2):
                        for col in range(j - 1, j + 2):
                            if 0 <= row < nRow and 0 <= col < nCol:
                                if (row == i and col == j) is False:
                                    searchRegion.add((row, col))
                    found = self.findRec(board, nRow, nCol, searchRegion, word[1:], {(i, j)})
                    if found:
                        return True
        return False

    def findRec(self, board, nRow, nCol, searchRegion, word, charPos):
        if len(word) == 0:
            return True
        for i, j in searchRegion:
            if board[i][j] == word[0]:
                charPos.add((i, j))
                nextSearchRegion = copy.deepcopy(searchRegion)
                for row in range(i-1, i+2):
                    for col in range(j-1, j+2):
                        if 0 <= row < nRow and 0 <= col < nCol:
                            if (row == i and col == j) is False:
                                nextSearchRegion.add((row, col))
                nextSearchRegion = {(k, l) for k, l in nextSearchRegion if (k, l) not in charPos}
                found = self.findRec(board, nRow, nCol, nextSearchRegion, word[1:], charPos)
                charPos.remove((i, j))
                if found:
                    return True
        return False

s = Solution()
b = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
w = 'ABCB'
r = s.exist(b, w)
print(r)
