"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry, length = 0, len(digits)
        i = length - 1
        while i >= 0:
            if i == length-1:
                d = (digits[i]+carry+1) % 10
                carry = int((digits[i] + carry + 1)/10)
            else:
                d = (digits[i]+carry) % 10
                carry = int((digits[i] + carry) / 10)
            digits[i] = d
            i -= 1
        if carry:
            digits = [1] + digits
        return digits


s = Solution()
digits = [9, 9]
print(s.plusOne(digits))