"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

"""


# 3
# 000 -> 001 -> 101 -> ...
#            -> 011
#            -> 000 (X)
#     -> 010 -> 110 -> ...
#            -> 011
#     -> 100 -> 110 -> ...
#            -> 101


class Solution(object):

    result = None

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return []
        self.result = []
        self.grayCodeRec(self.allPermutation(n), [])
        return self.result

    def toInt(self, str):
        for i in enumerate(str[::-1]):
            pass

    def allPermutation(self, n):
        res = ['0', '1']
        for i in range(1, n):
            resWithZero = [s+'0' for s in res]
            resWithOne = [s+'1' for s in res]
            res = resWithOne + resWithZero
        return res

    def grayCodeRec(self, notUsed, used):
        if len(notUsed) == 0:
            self.result = used
            return True
        for s in notUsed:
            if not used or self.oneDiff(s, used[-1]):
                notUsed.remove(s)
                used.append(s)
                if self.grayCodeRec(notUsed, used):
                    return True
                notUsed.append(s)
                used.remove(s)
        return False

    def oneDiff(self, s1, s2):
        numDiff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                numDiff += 1
                if numDiff > 1:
                    return False
        return numDiff == 1


s = Solution()
r = s.grayCode(4)
print(r)













