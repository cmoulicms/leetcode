from typing import List


numbers = [2,7,11,15,20]
target = 26

class Solution:
    def twoSum(self, numbers: List[int], target: int):
        low = 0
        high = len(numbers) - 1

        while low < high:
            sum = numbers[low] + numbers[high]

            if sum == target:
                return low, high
            elif sum < target:
                low += 1
            else:
                high -=1
        return -1,-1
    

my_object = Solution()
return_data = my_object.twoSum(numbers, target)
print(return_data)
                


