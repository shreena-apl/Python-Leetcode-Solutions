# Find All Duplicates in an Array

from collections import Counter
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_list=[]
        my_dict = Counter(nums)
        for key,value in my_dict.items():
            if value>=2:
                my_list.append(key)
        #print(my_list)
        return(my_list)