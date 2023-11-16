from typing import List

nums = [0,0]
class Solution:
    def max_consecutive_ones(self, nums: List[int]) -> int:
        count = 0
        maxones = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 1:
                count += 1
                if count > maxones:
                    maxones = count
            else:
                count = 0
        return maxones

my_object = Solution()
return_data = my_object.max_consecutive_ones(nums)
print(return_data)