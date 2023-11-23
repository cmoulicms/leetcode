# 2563 Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:
# (1) 0 <= i < j < n, and
# (2) lower <= nums[i] + nums[j] <= upper


from typing import List

nums = [0,1,7,4,4,5]
lower = 3
upper = 6

class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # below solution will exceed the time limit.
    def countFairPairs(self, nums: List[int], lower: int, upper: int):
        count = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] >= lower and nums[i] + nums[j] <= upper:
                    count += 1
        return count


obj = Solution()
res = obj.countFairPairs(nums, lower, upper)
print(res)


