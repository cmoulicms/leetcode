# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
from typing import List

nums = [3, 4, 5, 7, 8, 2]
target = 14

class Solution:
    # Below solution is O(n^2) Time complexity -> Quadratic.
    # def twoSum(self,nums:List[int],tar: int):
        # for i in nums:
        #     for j in nums:
        #         if(i+j == tar):
        #             return i,j

    # using hashset to return true or false
    # def twoSum(self, nums:List[int],tar:int):
    #     mySet = set()

    #     for i in range(len(nums)):
    #         x = tar - nums[i]
    #         if x in mySet:
    #             return True
    #         mySet.add(nums[i])
    #     return False
    
    # using hashmap need more information like indices.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)

        for i in range(n):
            x = target - nums[i]
            if x in map:
                return [map[x], i]
            map[nums[i]] = i
        return []


my_object = Solution()
return_data = my_object.twoSum(nums, target)
print(return_data)
