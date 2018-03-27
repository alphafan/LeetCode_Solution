"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()",
which has length = 4.
"""


class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Two pointer solution
        # Valid condition:
        #   number of left paren == number of right paren
        length = len(s)
        nLeft, nRight = 0, 0
        ans = 0
        for char in s:
            if char == '(':
                nLeft += 1
            else:
                nRight += 1
            if nLeft == nRight:
                ans = max(ans, nLeft*2)
            if nLeft < nRight:
                nLeft, nRight = 0, 0
        nLeft, nRight = 0, 0
        for char in s[::-1]:
            if char == '(':
                nLeft += 1
            else:
                nRight += 1
            if nLeft == nRight:
                ans = max(ans, nLeft*2)
            if nLeft > nRight:
                nLeft, nRight = 0, 0
        return ans
