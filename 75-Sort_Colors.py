"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 下午3:44
@Author  : Yang "Jan" Xiao 
@Description : 75-Sort_Colors
"""


class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1  # three pointers

        while white <= blue:
            if nums[white] == 0:  # if white point red, swap the position of two node.
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]  # if white point blue, swap the position of two node.
                blue -= 1


if __name__ == '__main__':
    solution = Solution()
    test = [2, 0, 2, 1, 1, 0]
    solution.sortColors(test)
    print(test)
