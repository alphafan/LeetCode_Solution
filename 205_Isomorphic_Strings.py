"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters. No two characters may map to the
same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

"""

from collections import defaultdict


def isIsomorphic(s, t):
    d1, d2 = defaultdict(int), defaultdict(int)
    for c1, c2 in zip(s, t):
        d1[c1] += 1
        d2[c2] += 1
        if d1[c1] != d2[c2]:
            return False
    return True


r = isIsomorphic('peptr', 'paper')
print(r)
