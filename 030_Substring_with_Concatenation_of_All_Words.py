"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a
concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

from collections import Counter
import copy


class Solution(object):

    """ TODO: Still have bugs.... """

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        m, n, results = len(words), len(words[0]), []
        for r in range(n):
            ss = [s[r:r+n] for r in range(r, len(s), n)]
            i = L = R = 0
            need, missing = Counter(words), len(words)
            for j, sub in enumerate(ss):
                if sub in need:
                    missing -= need[sub] > 0
                    need[sub] -= 1
                    if not missing:
                        while i < j and need[ss[i]] < 0:
                            need[ss[i]] += 1
                            i += 1
                        if not R or j - i <= R - L:
                            L, R = i, j
                            index = r+i*n
                            print(index)
                            results.append(index)
                else:
                    # Current sub string not in need, re-init
                    need, missing = Counter(words), len(words)
                    i = j
        return results



sol = Solution()
s = 'barfoofoobarthefoobarman'
words = ['bar', 'foo']
sol.findSubstring(s, words)

