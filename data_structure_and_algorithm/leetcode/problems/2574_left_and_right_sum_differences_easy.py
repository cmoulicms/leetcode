# 2574. Left and Right Sum Differences
from typing import List


nums = [10,4,8,3]

class Solution:

    def leftRightDifference(self, nums: List[int]):
        leftSum: List[int] = []
        for i in range(0, len(nums)):
            leftSum[i] += nums[i-1]
        print(leftSum)


obj = Solution()
res = obj.leftRightDifference(nums)
print(res)