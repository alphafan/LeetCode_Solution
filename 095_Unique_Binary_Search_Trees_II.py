"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreeHelper(1, n)

    def generateTreeHelper(self, start, end):

        result = []

        if start > end:
            return None

        for i in range(start, end+1):

            leftTreeNodes = self.generateTreeHelper(start, i-1)
            rightTreeNodes = self.generateTreeHelper(i+1, end)
            for leftNode in leftTreeNodes:
                for rigthNode in rightTreeNodes:
                    root = TreeNode(i)
                    root.left = leftNode
                    root.right = rigthNode
                    result.append(root)

        return result

