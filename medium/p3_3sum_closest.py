# 3Sum Closest

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
    
        result_sum = nums[0] + nums[1] + nums[2]
        min_diff = float('inf')

        for i in range(0, len(nums)-2):
            left = i+1
            right = len(nums)-1  
            while(left < right):
                sumof= nums[i] + nums[left] + nums[right]
                if sumof == target:
                    return target
                elif sumof < target:
                    left+=1
                else:
                    right-=1

                diff_to_tar = abs(sumof-target)
                if diff_to_tar < min_diff:
                    result_sum = sumof
                    min_diff = diff_to_tar
        return result_sum