# Definition for singly-linked list.
from typing import Optional

from LinkedList_Testcase import create_linked_list, print_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([-1, 5, 3, 4, 0])
    print(print_linked_list(s.middleNode(head)))

