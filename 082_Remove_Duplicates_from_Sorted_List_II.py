"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        node = ListNode('prev')
        node.next = head
        prev = node
        while node.next.next:
            while node.next.next and node.next.val == node.next.next.val:
                node.next = node.next.next
            node = node.next
            if node.next is None:
                break
        return prev.next


a, b, c, d = (ListNode(1) for _ in range(4))
e, f, g = (ListNode(2) for _ in range(3))
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
s = Solution()
h = s.deleteDuplicates(a)
print(h)