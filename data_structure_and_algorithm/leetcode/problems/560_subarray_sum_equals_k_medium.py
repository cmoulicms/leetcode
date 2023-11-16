from typing import List

nums = [1,2,3]
k = 3
class Solution:
    def subArraySum(self, nums: List[int], k:int):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == k:
                    count += 1
            return count    

obj = Solution()
# obj.subArraySum(nums, k)
print(obj.subArraySum(nums, k))
