"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 下午3:28
@Author  : Yang "Jan" Xiao 
@Description : 179-Largest_Number
"""


class compare(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest = sorted([str(v) for v in nums], key=compare)  # sort
        largest = ''.join(largest)  # convert the integer to string

        return '0' if largest[0] == '0' else largest  # if the first number is zero, the other must also be zero.


if __name__ == '__main__':
    solution = Solution()
    test = [0, 0, 5]
    print(solution.largestNumber(test))
