"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        if ls > lp:
            return False
        i = 0
        while i < ls-lp+1:
            if self.isMatchFromStart(s[i:], p[1:]):
                return True
            i += 1
        return False

    def isMatchFromStart(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Divide and conquer
        ls, lp = len(s), len(p)
        if ls < lp:
            return False
        if lp == 0:
            return True
        if p[0] == '.' or p[0] == s[0]:
            return self.isMatchFromStart(s[1:], p[1:])
        elif p[0] == '*':
            for i in range(0, ls-lp+1):
                if self.isMatchFromStart(s[1:], p[1:]):
                    return True
            return False
        else:
            return False


s = Solution()
r = s.isMatchFromStart('abcde', 'ab.*e')
print(r)
