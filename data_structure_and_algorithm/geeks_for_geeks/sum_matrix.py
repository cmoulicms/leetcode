from typing import List

matrix = [[3, 4, 9, 100],
          [2, 1, 59,30], 
          [22,-90,43,89]]
row = 0
column = 3
class Solution:

    def sumMatrix(self, nums: List[List[int]], row: int, column: int):
        sum = 0
        for i in range(0, row+1):
            for j in range(0, column+1):
                sum += nums[i][j]
        return sum

    
obj = Solution()
res = obj.sumMatrix(matrix,row, column)
print(res)