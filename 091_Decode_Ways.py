"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 1
        if len(s) == 1:
            if s == '0':
                return 0
            return 1
        first = self.numDecodings(s[1:]) if s[0] != '0' else 0
        second = self.numDecodings(s[2:]) if 9 < int(s[:2]) < 27 else 0
        return first + second


s = Solution()
r = s.numDecodings('21321')
# 1 2 2 1
# 12 2 1
# 1 2 21
# 1 22 1
# 12 21
print(r)