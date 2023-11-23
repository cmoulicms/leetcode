from typing import List

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)

        for i in range(0,n):

            sum += mat[i][i]

            sum += mat[n-1-i][i]

        if n % 2 != 0:
            sum -= mat[n//2][n//2]
        return sum


obj = Solution()
print(obj.diagonalSum(matrix))
