"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 上午1:17
@Author  : Yang "Jan" Xiao 
@Description : 148-Sort List
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # if the head is single node, return.
            return head
        dummy = ListNode()
        dummy.next = head  # dummy indicates the head of head.
        fast = dummy
        slow = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next  # two pointers to iter the linkedlist

        l1 = self.sortList(slow.next)  # l1 pointer points at the middle of the linkedlist
        slow.next = None  # we should isolate the two sub linkedlist by set slow.next points at none.
        l2 = self.sortList(dummy.next)  # l2 pointer points at the head of the linkedlist

        return self.merge_sort(l1, l2)  # execute the merge sort

    def merge_sort(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode()
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return dummy.next  # we merge two sub linkedlist to one sorted linkedlist


if __name__ == "__main__":
    solution = Solution()
    head = [-1, 5, 3, 4, 0]
    test = ListNode(0)
    dummy = test
    for i in range(len(head)):
        test.val = head[i]
        print(test.val)
        test.next = ListNode()
        test = test.next
    while dummy.next:
        print(dummy.val)
        dummy = dummy.next
    print(solution.sortList(dummy))
