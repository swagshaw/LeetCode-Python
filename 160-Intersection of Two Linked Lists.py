# Definition for singly-linked list.
from typing import Optional

from LinkedList_Testcase import create_linked_list, print_linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        while A is not B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


if __name__ == '__main__':
    s = Solution()
    headA = create_linked_list([-1, 5, 3, 4, 0])
    headB = create_linked_list([3, 4, 0])
    print(print_linked_list(s.getIntersectionNode(headA,headB)))
