"""
Given a string S and a string T, find the minimum window in S
which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will
always be only one unique minimum window in S.
"""

from collections import Counter
from collections import defaultdict


class Solution(object):

    def minWindow(self, s, t):
        i, I, J = 0, 0, 0
        need, missing = Counter(t), len(t)
        for j, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j-i < J-I:
                    I, J = i, j
        return s[I:J]


s = Solution()
r = s.minWindow('aaaaa', 'aa')
print(r)
