# Definition for singly-linked list.
from typing import Optional

from LinkedList_Testcase import create_linked_list, print_linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow


if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([-1, 5, 3, 4, 0, 3, 4])
    print(print_linked_list(s.detectCycle(head)))
