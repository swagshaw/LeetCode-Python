# Definition for singly-linked list.
from typing import Optional

from LinkedList_Testcase import create_linked_list, print_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        o = head
        p = ehead = head.next

        while head and head.next:
            o.next = p.next
            p.next = p.next.next

            o = o.next
            p = p.next

            if not p:
                break

        o.next = ehead

        return head


if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([-1, 5, 3, 4, 0])
    print(print_linked_list(s.oddEvenList(head)))
