"""
537. Complex Number Multiplication

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
"""

import unittest


class Complex(object):

    def __init__(self, real: int, imag: int):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return '{}+{}i'.format(self.real, self.imag)

    def __hash__(self):
        return hash(self.real) ^ hash(self.imag)

    def __eq__(self, other):
        if isinstance(other, Complex):
            if self.real == other.real and self.imag == other.imag:
                return True
        return False

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    @staticmethod
    def valueOf(s: str):
        """ Build a Complex object from string """
        hasImag = 'i' in s
        if hasImag:
            hasReal = '+' in s
            if hasReal:
                realStr, imagStr = s.split('+')
                imagStr = imagStr[:-1]
                real = int(realStr)
                imag = int(imagStr)
            else:
                realStr, imagStr = '', s[:-1]
                real = 0
                imag = int(imagStr)
        else:
            realStr, imagStr = s, ''
            real = int(realStr)
            imag = 0
        return Complex(real, imag)


class TestComplex(unittest.TestCase):

    def test_create_from_string_1(self):
        s = '1+1i'
        c = Complex.valueOf(s)
        self.assertEqual(c.real, 1)
        self.assertEqual(c.imag, 1)

    def test_create_from_string_2(self):
        s = '1+-2i'
        c = Complex.valueOf(s)
        self.assertEqual(c.real, 1)
        self.assertEqual(c.imag, -2)

    def test_create_from_string_3(self):
        s = '1'
        c = Complex.valueOf(s)
        self.assertEqual(c.real, 1)
        self.assertEqual(c.imag, 0)

    def test_create_from_string_4(self):
        s = '-2i'
        c = Complex.valueOf(s)
        self.assertEqual(c.real, 0)
        self.assertEqual(c.imag, -2)

    def test_create_from_string_5(self):
        s = '-1+-2i'
        c = Complex.valueOf(s)
        self.assertEqual(c.real, -1)
        self.assertEqual(c.imag, -2)

    def test_mul_1(self):
        s1, s2 = '1+-1i', '1+-1i'
        c1, c2 = Complex.valueOf(s1), Complex.valueOf(s2)
        result = c1 * c2
        self.assertEqual(result, Complex.valueOf('-2i'))

    def test_mul_2(self):
        s1, s2 = '1+1i', '1+1i'
        c1, c2 = Complex.valueOf(s1), Complex.valueOf(s2)
        result = c1 * c2
        self.assertEqual(result, Complex.valueOf('2i'))


unittest.main()
