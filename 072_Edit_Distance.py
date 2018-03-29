"""
Given two words word1 and word2, find the minimum number of steps required to
convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""


class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # f(i, j) : the step that needs for convert from word1[i] -> word2[j]
        # case 1: word1[i] == word2[j]
        #   f(i, j) == f(i-1, j-1)
        # case 2: word1[i] != word2[j]
        #   f(i, j) == 1 + min(f(i-1, j), f(i-1, j-1), f(i, j-1))
        #       - f(i-1, j) -- insert at word1[i]
        #       - f(i-1, j-1) -- replace at word1[i]
        #       - f(i, j-1) -- delete at word2[j]
        # base case:
        #   f(k, 0) == f(0, k) == k

        m, n = len(word1), len(word2)

        d = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            d[i][0] = i
        for i in range(n+1):
            d[0][i] = i

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    d[i+1][j+1] = d[i][j]
                else:
                    d[i+1][j+1] = 1 + min(d[i][j], d[i+1][j], d[i][j+1])

        return d[m][n]


s = Solution()
r = s.minDistance('abc', 'b')
print(r)