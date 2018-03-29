"""
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
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
    """ Still bug ... """

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Step 1: Get the Kth last element
        fast, slow = head, head
        length = 0
        for _ in range(k):
            fast = fast.next
            length += 1
            if fast is None:
                raise Exception('List is shorter than k')
        while fast:
            length += 1
            fast = fast.next
            slow = slow.next
        node = slow
        while node.next:
            node = node.next
        print(head)
        node.next = head
        head = ListNode(node.val)
        print(length)
        for _ in range(length):
            node = node.next
            head.next = ListNode(node.val)
        return head


s = Solution()
a, b, c, d, e = (ListNode(i) for i in 'abcde')
a.next, b.next, c.next, d.next = b, c, d, e
print(s.rotateRight(a, 2))
