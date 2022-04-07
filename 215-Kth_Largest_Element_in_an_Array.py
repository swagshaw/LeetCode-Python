"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 下午4:28
@Author  : Yang "Jan" Xiao 
@Description : 215.-Kth_Largest_Element_in_an_Array
"""
import random
from typing import List


class Solution(object):
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     return sorted(nums, reverse=True)[k - 1]

    # def findKthLargest(self, nums, k):
    #     # build min heap
    #     heapq.heapify(nums)
    #     # remove n - k smallest number
    #     while len(nums) > k:
    #         heapq.heappop(nums)
    #     return nums[0]
    #     #return heapq.nlargest(k, nums)[-1]

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


if __name__ == '__main__':
    solution = Solution()
    test = [2, 4, 6, 8, 10]
    print(solution.findKthLargest(test, 2))
