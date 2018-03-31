"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        pathSum, allPaths = 0, []

        def allPathToLeave(root, path):
            if root.left is None and root.right is None:
                allPaths.append(path)
            if root.left:
                allPathToLeave(root.left, path + [root.left])
            if root.right:
                allPathToLeave(root.right, path + [root.right])

        allPathToLeave(root, [root])

        for path in allPaths:
            numStr = ''.join([str(n) for n in path])
            num = int(numStr)
            pathSum += num

        return pathSum


a, b, c, d, e, f, g = (TreeNode(i) for i in range(1, 8))
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

h = TreeNode(0)

s = Solution()
r = s.sumNumbers(h)
print(r)









