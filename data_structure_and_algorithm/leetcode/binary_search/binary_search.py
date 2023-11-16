# Approach 1:Find the exact value
from typing import List

nums = [2, 3, 4, 5, 6, 7, 8]
target = 5


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle

            elif target > nums[middle]:
                left = middle + 1

            elif target < nums[middle]:
                right = middle - 1

        return -1


myObj = Solution()
print(myObj.search(nums, target))
