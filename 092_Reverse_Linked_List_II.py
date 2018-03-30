"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        repr_str, node = '', self
        while node:
            repr_str += str(node.val) + ' -> '
            node = node.next
        return repr_str + 'None'


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m != 1:
            i, prev, node = 0, None, head
            while i < m-1:
                prev = node
                node = node.next
                i += 1
            prev.next = self.reverseKNodes(node, n-m+1)
        else:
            head = self.reverseKNodes(head, n-m+1)
        return head

    def reverseKNodes(self, head, k):
        if head is None or head.next is None:
            return head
        pre, cur, i = None, head, 0
        while i < k:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            i += 1
        node = pre
        while node.next:
            node = node.next
        node.next = cur
        return pre


s = Solution()
a, b, c, d, e = (ListNode(i) for i in 'abcde')
a.next, b.next, c.next, d.next = b, c, d, e
print(s.reverseBetween(a, 2, 4))
