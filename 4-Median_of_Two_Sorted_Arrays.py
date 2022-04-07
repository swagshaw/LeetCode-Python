"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 下午9:44
@Author  : Yang "Jan" Xiao 
@Description : 4-Median_of_Two_Sorted_Arrays
"""
import random
from typing import List


class Solution:
    def findKthLargest(self, nums, k):
        # shuffle nums to avoid n*n
        random.shuffle(nums)
        return self.quickSelection(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelection(self, nums, start, end, k):
        if start > end:
            return float('inf')
        pivot = nums[end]  # the val of the end of list
        left = start
        for i in range(start, end):
            if nums[i] <= pivot:
                # swap left and i
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[end] = nums[end], nums[left]
        if left == k:
            return nums[left]
        elif left < k:
            return self.quickSelection(nums, left + 1, end, k)
        else:
            return self.quickSelection(nums, start, left - 1, k)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        totalLength = len(nums)
        if totalLength % 2 == 1:
            return self.findKthLargest(nums, (totalLength + 1) // 2)
        else:
            return (self.findKthLargest(nums, totalLength // 2) + self.findKthLargest(nums, totalLength // 2 + 1)) / 2


if __name__ == '__main__':
    solution = Solution()
    test1 = [1, 3, 5, 7]
    test2 = [2, 4, 6, 8, 10]
    print(solution.findMedianSortedArrays(test1, test2))
