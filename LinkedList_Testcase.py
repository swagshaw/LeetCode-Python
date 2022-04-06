"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 上午1:38
@Author  : Yang "Jan" Xiao 
@Description : LinkedList_Testcase
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == '__main__':
    head = [-1, 5, 3, 4, 0]
    test = ListNode(0)
    dummy = test

    for i in range(len(head)):
        test.val = head[i]
        # print(test.val)
        test.next = ListNode()
        test = test.next

    while dummy.next:
        # print(dummy.val)
        dummy = dummy.next
