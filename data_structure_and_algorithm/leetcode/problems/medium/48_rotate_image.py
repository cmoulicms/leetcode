# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

from typing import List

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14, 15,16]]
# matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]


class Solution:
    def rotate(self, nums: List[List[int]]):
        mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0]]
        # left to right
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums[i])):
        #         print(nums[i][j])

        # right to left
        # for i in range(0, len(nums)):
        #    for j in range(len(nums[i])-1, -1, -1):
        #         print(nums[i][j])
        
        # top to bottom
        # for j in range(0, len(nums[0])):
        #     for i in range(0, len(nums)):
        #         print(nums[i][j])

        # bottom to top
        # for j in range(0, len(nums[0])):
        #     for i in range(len(nums)-1, -1, -1):
        #         print(nums[i][j])

        # row -> top to bottom 1st column
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         mat[j][i] = nums[i][j]
        # print(mat)

        # row -> bottom to top 1st column. 90degree anti-clockwise
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         mat[len(nums)-1-j][i] = nums[i][j]
        # print(mat)

        # row -> top to bottom last column. 90degree clockwise
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         mat[j][len(nums)-1-i] = nums[i][j]
        # print(mat)

        # column -> reverse
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         mat[i][len(nums)-1-j] = nums[i][j]
        # print(mat)

        # row -> reverse
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         mat[len(nums)-1-i][j] = nums[i][j]
        # print(mat)
        
        # rigth to left -> ladder
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)-i):
        #        print(nums[i][j])

        # left to right -> ladder
        for i in range(0, len(nums)):
            for j in range(0, len(nums)-i):
               print(nums[i][j])





obj = Solution()
res = obj.rotate(matrix)
# print(matrix)
