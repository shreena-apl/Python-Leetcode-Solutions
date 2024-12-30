# Merge Intervals

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         result=[]
#         intervals.sort()
#         for i in range(1, len(intervals)):
#             if intervals[i][0]<=intervals[i-1][1]:
#                 result = result + intervals[[0][0],[1][1]]
#             else:
#                 result+=intervals
#         return result

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        result=[]
        intervals.sort()

        new_interval = intervals[0]
        result.append(new_interval)

        for interval in intervals:
            if interval[0] <= new_interval[1]:
                new_interval[1] = max(new_interval[1], interval[1])
            else:
                new_interval = interval
                result.append(new_interval)
        return result