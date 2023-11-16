from typing import List
nums = [1, 2, 3, 4, 5]
class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
                

obj = Solution()
res = obj.containsDuplicate(nums)
print(res)