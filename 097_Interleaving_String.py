"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""


class Solution(object):

    memo = {}

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 != l2 or l1*2 != l3:
            return False
        return self.isInterLeaveHelper(s1, s2, s3)

    def isInterLeaveHelper(self, s1, s2, s3):
        if (s1, s2, s3) in self.memo:
            return self.memo[(s1, s2, s3)]
        if s1 == '' or self.isCombine(s1, s2, s3):
            self.memo[(s1, s2, s3)] = True
            return True
        length = len(s1)
        for i in range(1, length):
            if self.isCombine(s1[:i], s2[:i], s3[:2*i]):
                if self.isInterLeaveHelper(s1[i:], s2[i:], s3[2*i:]):
                    self.memo[(s1, s2, s3)] = True
                    return True
        self.memo[(s1, s2, s3)] = False
        return False

    def isCombine(self, s1, s2, s3):
        return s1+s2 == s3 or s2+s1 == s3


s = Solution()
r = s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
print(r)
