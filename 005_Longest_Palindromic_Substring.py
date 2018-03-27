"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"
"""


class Solution(object):
    """ Expand at center """

    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        maxLength = 0
        for i in range(len(s)-1):
            res1 = self.expandAtCenter(s, i, i)
            res2 = self.expandAtCenter(s, i, i+1)
            if max(res1, res2) > maxLength:
                maxLength = max(res1, res2)
        return maxLength

    def expandAtCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

s = Solution()
r = s.longestPalindrome('abaaba')
print(r)
