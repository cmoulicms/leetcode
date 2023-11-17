# 2778. Sum of Squares of Special Elements

# You are given a 1-indexed integer array nums of length n.

# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

# Return the sum of the squares of all special elements of nums

from typing import List


arr = [2, 7, 1, 19, 18, 3]


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_suqares = 0
        for i in range(0, n):
            if n % (i+1) == 0:
                sum_of_suqares += nums[i] ** 2

        return sum_of_suqares


obj = Solution()
res = obj.sumOfSquares(arr)
print(res)
