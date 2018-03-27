"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, ans, charIndex = 0, 0, 0, {}
        while i < len(s) and j < len(s):
            if s[j] not in charIndex:
                charIndex[s[j]] = j
                j += 1
                ans = max(ans, j-i)
            else:
                i = charIndex[s[j]] + 1
                charIndex.pop(s[j])
        return ans


s = Solution()
r = s.lengthOfLongestSubstring('abcdefghuiausiay')
print(r)

