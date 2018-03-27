"""

Given n pairs of parentheses, write a function to
generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generate(n, '', 0, 0)

    def generate(self, n, string, left, right):
        if left == n and right == n:
            print(string)
        if left < n:
            self.generate(n, string+'(', left+1, right)
        if right < left:
            self.generate(n, string+')', left, right+1)

s = Solution()
s.generateParenthesis(3)