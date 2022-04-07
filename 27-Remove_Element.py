"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 下午2:30
@Author  : Yang "Jan" Xiao 
@Description : 27-Remove_Element
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        use slow, fast two pointers
        :param nums:
        :param val:
        :return:
        """
        fast = slow = 0
        while fast < len(nums):  # fast pointers to iter the whole array
            if nums[fast] != val:  # whenever the item is not equal to val, replace the value of slow pointed, and move
                nums[slow] = nums[fast]
                slow += 1

            fast += 1
        return slow


if __name__ == '__main__':
    solution = Solution()
    test = [3, 2, 2, 3]
    val = 3
    print(solution.removeElement(test, val))
    print(test[:solution.removeElement(test, val) - 1])
