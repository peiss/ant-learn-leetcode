package p206_Reverse_Linked_List;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newhead = null;
        ListNode temp;
        while (null != head) {
            temp = head;
            head = head.next;
            temp.next = newhead;
            newhead = temp;
        }
        return newhead;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, null)))));

        ListNode temp = head;
        while (null != temp) {
            System.out.println(temp.val);
            temp = temp.next;
        }

        Solution s = new Solution();
        ListNode newHead = s.reverseList(head);
        System.out.println("####");
        while (null != newHead) {
            System.out.println(newHead.val);
            newHead = newHead.next;
        }
    }
}