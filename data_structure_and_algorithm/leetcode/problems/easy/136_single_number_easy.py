# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

from typing import List

nums = [2,5,2,1]
class Solution:
    
    def singleNumber(self, nums: List[int]):
        a = 0
        for i in nums:
            a ^= i
        return a

obj = Solution()
res = obj.singleNumber(nums)
print(res)