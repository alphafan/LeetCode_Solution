"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i, c1, in enumerate(num1[::-1]):
            for j, c2 in enumerate(num2[::-1]):
                n1, n2 = ord(c1) - ord('0'), ord(c2) - ord('0')
                mul = n1 * n2
                p1 = len(num1) + len(num2) - i - j - 1
                p2 = p1 - 1
                res[p1] += mul % 10
                res[p2] += int(mul/10)
        res = [str(i) for i in res]
        res = ''.join(res)
        print(res)


s = Solution()
s.multiply('12', '23')