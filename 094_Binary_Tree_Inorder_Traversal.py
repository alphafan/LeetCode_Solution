"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, node = [], root
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res


s = Solution()
a, b, c, d, e, f, g = (TreeNode(i) for i in 'abcdefg')
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g
s.inorderTraversal(a)