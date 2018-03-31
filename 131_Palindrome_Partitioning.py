"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

from collections import defaultdict


class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        partitions = []

        def partitionHelper(s, index, splitStrings, posDict):
            if index == len(s):
                partitions.append(splitStrings)
                return
            nextSplitIndex = posDict[index]
            for nextIndex in nextSplitIndex:
                partitionHelper(s, nextIndex,
                                splitStrings + [s[index:nextIndex]], posDict)

        partitionHelper(s, 0, [], self.findAllPalindromes(s))

        return partitions

    def findAllPalindromes(self, s):
        """ Find all palindromes in string

        Args:
            s: String to find palindromes

        Returns:
            posDict: startIndex -> set of endIndex of palindrome strings
        """
        posDict = defaultdict(set)
        for i, char in enumerate(s):
            self.expandFromCenter(s, i, i, posDict)
            self.expandFromCenter(s, i, i + 1, posDict)
        return posDict

    def expandFromCenter(self, s, left, right, posDict):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            posDict[left].add(right + 1)
            left -= 1
            right += 1