"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution(object):

    memo = {0: 1, 1: 1, 2: 2}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        res = 2 * self.numTrees(n-1)
        for i in range(1, n-1):
            res += self.numTrees(i) * self.numTrees(n-i-1)
        self.memo[n] = res
        return res


s = Solution()
r = s.numTrees(4)
print(r)
