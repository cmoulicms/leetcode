from typing import List

nums = [12,345,2,6,7896]

class Solution:
    
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        digitCount = 0
        for i in range(0, len(nums)):
            number = nums[i]
            while number != 0:
                digit = number % 10
                digitCount += 1
                number = digit 

            if digitCount % 2 == 0:
                count += 1
        return count

obj = Solution()
res = obj.findNumbers(nums)
print(res)