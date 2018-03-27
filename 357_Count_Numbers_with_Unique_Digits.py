"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100,
excluding [11,22,33,44,55,66,77,88,99])

"""


class Solution(object):

    """
    f(1) = 10
    f(2) = 9*9
    f(3) = 9*9*8
    f(4) = 9*9*8*7
    f(5) = ...
    """

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 or n >= 10:
            return 0
        if n == 1:
            return 10
        res, tmp, i = 10, 9, 1
        while i < n:
            tmp = (10-i) * tmp
            res += tmp
            i += 1
        return res
