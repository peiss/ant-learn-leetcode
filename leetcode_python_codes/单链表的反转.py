class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newhead = None

        while head:
            temp = head
            head = head.next
            temp.next = newhead
            newhead = temp
        return newhead


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(
        3, ListNode(4, ListNode(5, None)))))
        
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

    s = Solution()
    newhead = s.reverseList(head)
    print("#"*10)
    while newhead:
        print(newhead.val)
        newhead = newhead.next
