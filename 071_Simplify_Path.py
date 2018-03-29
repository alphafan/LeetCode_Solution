"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""


class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        folders = [p for p in path.split('/') if p not in ['', '.']]
        for f in folders:
            if f != '..':
                stack.append(f)
            else:
                if len(stack) != 0:
                    stack.pop()
            print(stack)
        if path[0] == '/':
            return '/' + '/'.join(stack)
        return '/'.join(stack)


s = Solution()
p = '/a/../b'
r = s.simplifyPath(p)
print(r)
