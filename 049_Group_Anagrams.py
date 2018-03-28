"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""

from collections import defaultdict


class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedStrs = [''.join(sorted(s)) for s in strs]
        strDict = defaultdict(list)
        for i, s in enumerate(sortedStrs):
            strDict[s].append(i)
        res = [[strs[i] for i in indices] for indices in strDict.values()]
        return res


s = Solution()
g = ["eat", "tea", "tan", "ate", "nat", "bat"]
r = s.groupAnagrams(g)
print(r)
