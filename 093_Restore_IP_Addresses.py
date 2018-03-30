"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.findIP(s, 4, [], len(s), results)
        return results

    def findIP(self, s, count, partial, length, results):
        if count == 0:
            if length == len(''.join(partial)):
                results.append('.'.join(partial))
            return
        if count == 1:
            if len(s) == 0 or len(s) > 3:
                return
            if len(s) == 1:
                self.findIP('', 0, partial + [s], length, results)
                return
            if s[0] == '0':
                return
            if len(s) == 3 and int(s) > 255:
                return
            self.findIP('', 0, partial + [s], length, results)
        if len(s) < count or len(s) > 3 * count:
            return
        if s[0] == '0':
            self.findIP(s[1:], count-1, partial + ['0'], length, results)
            return
        if len(s) > 1:
            self.findIP(s[1:], count-1, partial+[s[:1]], length, results)
        if len(s) > 2:
            self.findIP(s[2:], count-1, partial+[s[:2]], length, results)
        if len(s) > 3 and int(s[:3]) < 256:
            self.findIP(s[3:], count-1, partial+[s[:3]], length, results)


ip = '010010'
s = Solution()
r = s.restoreIpAddresses(ip)
print(r)
