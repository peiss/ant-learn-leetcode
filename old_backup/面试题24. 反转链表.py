# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_node = None
        while head:
            tmp = head.next
            head.next = new_node
            new_node = head

            head = tmp
        return new_node
