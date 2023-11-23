from typing import List

nums = [1,2,3]
k = 3
class Solution:
    def subArraySum(self, nums: List[int], k:int)->int:
        n = len(nums)
        total = 0
        index = 0
        count = 0
        while index < n:
            for i in range(index,n):
                total = nums[i] + total
                if total == k:
                    count += 1                
            index += 1
            total = 0
        return count   

obj = Solution()
res = obj.subArraySum(nums, k)
print(res)
