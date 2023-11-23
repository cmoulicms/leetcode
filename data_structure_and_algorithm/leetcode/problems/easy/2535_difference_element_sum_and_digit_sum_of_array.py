# 2535. Difference Between Element Sum and Digit Sum of an Array
# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.
from typing import List


nums = [1, 15, 6, 3]


class Solution:
    def differenceOfSum(self, nums: List[int]):
        element_sum = 0
        digit_sum = 0
        for i in range(0, len(nums)):
            element_sum += nums[i]
            while nums[i] > 0:
                digit_sum += nums[i] % 10
                nums[i] //= 10
        if element_sum > digit_sum:
            return element_sum - digit_sum
        else:
            return digit_sum - element_sum



obj = Solution()
res = obj.differenceOfSum(nums)
print(res)
