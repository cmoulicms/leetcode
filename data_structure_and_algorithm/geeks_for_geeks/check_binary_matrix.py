# Check Binary Matrix. It is also called Logical Matrix, Boolean Matrix, Relation Matrix\
# all elements either 0 or 1

from typing import List

matrix = [[0, 1, 1, 0],
          [0, 1, 1, 0], 
          [1, 0, 1, 11]]
class Solution:

    def checkBinaryMatrix(self, nums: List[List[int]]):
        maxElement = 0

        for i in range(0, len(nums)):
            for j in range(0, len(nums[i])):
                if nums[i][j] ==  0 or nums[i][j] == 1:
                    return True
        return False
    
obj = Solution()
print(obj.checkBinaryMatrix(matrix))