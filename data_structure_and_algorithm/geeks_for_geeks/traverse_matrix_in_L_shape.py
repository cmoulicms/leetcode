# Check Binary Matrix. It is also called Logical Matrix, Boolean Matrix, Relation Matrix\
# all elements either 0 or 1

from typing import List

matrix = [[0, 1, 2, 3],
          [4, 5, 6, 7], 
          [8, 9, 10, 11]]
class Solution:

    def traverseMatrixInLShape(self, nums: List[List[int]], n, m):
        
        # traverse in snake shape
        for j in range(0, m):
            if j % 2 == 0:
                for i in range(0, n):
                    print(nums[i][j])
            else:
                for i in range(n-1, -1, -1):
                    print(nums[i][j])

        # traverse matrix in L shape
        # for j in range(0, m):
 
        #     for i in range(0, n - j):
        #         print(nums[i][j])
 
        #     for k in range(j + 1, m):
        #         print(nums[n - 1 - j][k])

        # horizontal left to right
        # for i in range(0, n):
        #     for j in range(0, m):
        #         print(nums[i][j])

        # horizontal right to left
        # for i in range(0, n):
        #     for j in range(m-1, -1, -1):
        #         print(nums[i][j])

        # vertical top to bottom
        # for j in range(0, m):
        #     for i in range(0, n):
        #         print(nums[i][j])

        # vertical bottom to top
        # for j in range(0, m):
        #     for i in range(n-1, -1, -1):
        #         print(nums[i][j])
    
obj = Solution()
obj.traverseMatrixInLShape(matrix, len(matrix), len(matrix[0]))