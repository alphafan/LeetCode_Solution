"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

# Definition for singly-linked list.
import time


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

    def reverseKGroup(self, head, k):
        if not self.needReverse(head, k):
            return head
        head = self.reverseKNodes(head, k)
        i, prev, node = 0, None, head
        while i < k:
            prev = node
            node = node.next
            i += 1
        prev.next = self.reverseKGroup(node, k)
        return head

    def reverseKNodes(self, head, k):
        if head is None or head.next is None:
            return head
        prev, curr = None, head
        while curr and k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            k -= 1
        node = prev
        while node.next:
            node = node.next
        node.next = curr
        return prev

    def needReverse(self, head, k):
        while k > 0:
            if not head:
                return False
            head = head.next
            k -= 1
        return True


a, b, c, d, e, f, g = (ListNode(i) for i in 'abcdefg')
s = Solution()
a.next, b.next, c.next = b, c, d
d.next, e.next, f.next = e, f, g
print(s.reverseKGroup(a, 5))
