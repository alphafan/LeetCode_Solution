"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


class Solution(object):

    factorial = [0] + [1] * 9
    for i in range(2, 10):
        factorial[i] = factorial[i-1] * i

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n+1))
        res = ''
        while len(nums) > 0:
            i = self.getFirstNumber(nums, k)
            k -= nums.index(i) * self.factorial[len(nums)-1]
            nums.remove(i)
            res += str(i)
        return res

    def getFirstNumber(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        numPermForSubset = self.factorial[n-1]
        firstNum = int((k-1)/numPermForSubset)
        return nums[firstNum]


s = Solution()
r = s.getPermutation(5, 3)
print(r)
