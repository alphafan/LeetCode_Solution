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
        if s == '' or len(words) == 0:
            return []
        n = len(words)
        l = len(words[0])
        counter = Counter(words)
        ans = []
        for r in range(l):
            splitStrings = []
            for idx in range(r, len(s), l):
                splitStrings.append(s[idx:idx+l])
            m = len(splitStrings)
            if len(splitStrings) < n:
                continue
            i, j, c = 0, 0, copy.deepcopy(counter)
            while i < m and j < m:
                if splitStrings[j] in c:
                    if c[splitStrings[j]] == 0:
                        while i < j and splitStrings[i] != c[splitStrings[j]]:
                            c[splitStrings[i]] += 1
                            i += 1
                        # i += 1
                        # j += 1
                    else:
                        c[splitStrings[j]] -= 1
                        j += 1
                        if any(c.values()) is False:
                            # All words count are 0
                            print(r+l*i, r+l*j)
                            print(s[r+l*i:r+l*j])
                            ans.append(r+l*i)
                            i, j, c = i+1, i+1, copy.deepcopy(counter)
                            if j >= m:
                                break
                else:
                    j += 1
                    i = j
                    c = copy.deepcopy(counter)
        return ans

sol = Solution()
s = 'barfoofoobarthefoobarman'
words = ['bar', 'foo', 'the']
sol.findSubstring(s, words)

