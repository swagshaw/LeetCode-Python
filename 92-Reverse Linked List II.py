# Definition for singly-linked list.
from LinkedList_Testcase import create_linked_list, print_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        cur, pre = head, dummy
        for _ in range(left-1):
            cur = cur.next
            pre = pre.next

        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([-1, 5, 3, 4, 0])
    print(print_linked_list(s.reverseBetween(head, 1, 4)))
