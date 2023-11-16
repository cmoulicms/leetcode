# 2824: Given a 0-indexed integer array nums of length n and an integer target, 
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

# Topics: Array, Two Pointers, Sorting

from typing import List

nums = [-1,1,2,3,1]
target = 2
class Solution:
    # Time complexity O(n^2)
    # Space complexity O(1)
    def countPairs(self, nums: List[int], target: int):
        numberOfPairs = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    numberOfPairs += 1
        return numberOfPairs

obj = Solution()
res = obj.countPairs(nums, target)
print(res)