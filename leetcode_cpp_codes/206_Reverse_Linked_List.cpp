#include <iostream>
using namespace std;

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 public:
  ListNode* reverseList(ListNode* head) {
    ListNode* newhead = nullptr;
    ListNode* temp;
    while (head) {
      temp = head;
      head = head->next;
      temp->next = newhead;
      newhead = temp;
    }
    return newhead;
  }
};

int main() {
  ListNode node5 = ListNode(5, nullptr);
  ListNode node4 = ListNode(4, &node5);
  ListNode node3 = ListNode(3, &node4);
  ListNode node2 = ListNode(2, &node3);
  ListNode node1 = ListNode(1, &node2);
  ListNode* head = &node1;

  ListNode* temp = head;
  while (temp) {
    std::cout << temp->val << std::endl;
    temp = temp->next;
  }

  std::cout << "###" << std::endl;
  Solution s = Solution();
  ListNode* newhead = s.reverseList(head);
  while (newhead) {
    std::cout << newhead->val << std::endl;
    newhead = newhead->next;
  }
}

