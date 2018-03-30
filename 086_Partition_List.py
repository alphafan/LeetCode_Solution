"""
Given a linked list and a value x, partition it such that all nodes less
than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        repr_str = ''
        node = self
        while node:
            repr_str += str(node.val) + ' -> '
            node = node.next
        return repr_str + 'None'


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        rHead = ListNode(None)
        node, rNode = head, rHead
        while node:
            if node.val < x:
                if rNode.val is None:
                    rNode.val = node.val
                else:
                    rNode.next = ListNode(node.val)
                    rNode = rNode.next
            node = node.next
        node = head
        while node:
            if node.val >= x:
                if rNode.val is None:
                    rNode.val = node.val
                else:
                    rNode.next = ListNode(node.val)
                    rNode = rNode.next
            node = node.next
        return rHead


a, b, c, d = (ListNode(i) for i in [5, 3, 2, 5])
a.next = b
b.next = c
c.next = d
print(a)

s = Solution()
r = s.partition(a, 2)
print(r)
