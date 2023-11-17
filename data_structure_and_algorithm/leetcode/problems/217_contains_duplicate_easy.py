# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from typing import List
nums = [1, 2, 3, 4, 5]
class Solution:
    # Time complexity O(n^2)
    # Space complexity O(1)
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(0, len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time complexity O(n)
        # Space complexity O(n)
        mySet = set()
        for i in nums:
            if i in mySet:
                return True
            else:
                mySet.add(i)
        return False
            
                

obj = Solution()
res = obj.containsDuplicate(nums)
print(res)