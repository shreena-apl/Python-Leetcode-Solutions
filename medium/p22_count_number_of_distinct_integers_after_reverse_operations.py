# Count Number of Distinct Integers After Reverse Operations

from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        all_nums= nums+ [int(str(n)[::-1]) for n in nums]
        return len(set(all_nums))