from typing import List


nums = [1,2,3,7,5]
s = 12
class Solution:

    def subArraySum(self, nums: List[int],s: int):
        n = len(nums)
        total = 0
        index = 0
        while index < n:
            for i in range(index,n):
                total = nums[i] + total
                if total == s:
                    return index+1, i+1
                
            index += 1
            total = 0
        return -1

obj = Solution()
res = obj.subArraySum(nums,s)
print(res)