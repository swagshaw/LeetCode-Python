# Definition for singly-linked list.
from typing import Optional

from LinkedList_Testcase import create_linked_list, print_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     if not head.next:
    #         return head
    #
    #     n = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #
    #     return n
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        cur, pre = head, dummy

        while cur and cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp

        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([-1, 5, 3, 4, 0])
    print(print_linked_list(s.reverseList(head)))
