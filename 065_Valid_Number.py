"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
"""


class Solution(object):

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        numberSeen = False
        eSeen = False
        pointSeen = False
        numberAfterE = False
        for char in s:
            if '0' <= char <= '9':
                numberSeen = True
            elif char == '.':
                if not numberSeen or pointSeen:
                    return False
                pointSeen = True
            elif char == 'e':
                if not numberSeen:
                    return False
                eSeen = True
            elif char in ['+', '-']:
                pass
            else:
                return False

print(10e5)
