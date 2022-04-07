"""
# !/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/4/7 下午12:24
@Author  : Yang "Jan" Xiao 
@Description : 58-Merge Intervals
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()  # sort the intervals by the start
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            elif res[-1][1] >= intervals[i][0]:  # if end >= start, there are overlapping.
                res[-1][1] = max(intervals[i][1], res[-1][1])  # we should decide which one is the interval's end.
            else:
                res.append(intervals[i])  # else no overlapping, merge.

        return res


if __name__ == '__main__':
    solution = Solution()
    test = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(test))
