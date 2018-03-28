"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""


class Solution(object):

    # Add DP solution to make it faster

    memo = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0:
            return p == '' or (len(p) > 0 and p[0] == '*' and self.isMatch(s, p[1:]))
        if len(s) == 1:
            if len(p) == 0:
                return False
            elif len(p) == 1:
                if p == s or p == '?' or p == '*':
                    return True
                else:
                    return False
            else:
                if p[0] == '*':
                    return self.isMatch(s, p[1:])
                elif p[0] in ['?', s]:
                    return self.isMatch('', p[1:])
                else:
                    return False
        if len(s) >= 2:
            if len(p) == 0:
                return False
            if p[0] == '*':
                if p == '*':
                    return True
                else:
                    # More character after '*'
                    for i in range(len(s)):
                        if self.isMatch(s[i:], p[1:]):
                            return True
                    return False
            elif p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            elif p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return False


s = Solution()
r = s.isMatch("ho", "ho**")
print(r)
