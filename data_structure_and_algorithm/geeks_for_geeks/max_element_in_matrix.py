from typing import List

matrix = [[3, 4, 9, 100],
          [2, 1, 59,30], 
          [22,-90,43,89]]
class Solution:

    def findMaxElementInMatrix(self, nums: List[List[int]]):
        maxElement = 0

        for i in range(0, len(nums)):
            for j in range(0, len(nums[i])):
                if nums[i][j] > maxElement:
                    maxElement = nums[i][j]
        return maxElement
obj = Solution()
print(obj.findMaxElementInMatrix(matrix))