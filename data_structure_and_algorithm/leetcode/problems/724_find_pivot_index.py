from typing import List

nums = [1,7,3,6,5,6]

class Solution:
    def find_pivot_index(self,nums: List[int]):
        s = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (s - leftsum - x):
                return i
            leftsum += x
        return -1

my_object = Solution()
print(my_object.find_pivot_index(nums))