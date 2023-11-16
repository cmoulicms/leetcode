from typing import List

nums = [3, 4, 5, 7, 8, 2]
target = 15


# this solution is O(n^2) Quadratic
# class Solution:
#     def twoSum(self,nums:List[int],tar: int):
#         for i in nums:
#             for j in nums:
#                 if(i+j == tar):
#                     return i,j


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)

        for i in range(n):
            x = target - nums[i]
            if x in map:
                return [map[x], i]
            map[nums[i]] = i
            print(map)
        return []


my_object = Solution()
return_data = my_object.twoSum(nums, target)
print(return_data)
