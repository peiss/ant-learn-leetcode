# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(None)
        curr = dummy_node

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = l1
                l1=l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy_node.next
