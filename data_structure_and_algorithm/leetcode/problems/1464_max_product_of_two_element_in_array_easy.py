# Maximum Product of Two Elements in an Array

# Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
from typing import List

arrList = [3,4,5,2]

class Solution:

    def maxProduct(self, nums: List[int]):
        maxValue = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] -1) * (nums[j]-1) > maxValue:
                    maxValue = (nums[i] -1) * (nums[j]-1)
        return maxValue


obj = Solution()
res = obj.maxProduct(arrList)
print(res)
