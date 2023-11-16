# Time O(n^2)
# Space O(1)
# Stable Sort 

from typing import List

arr = [7,3,2,5,6,10,9,8,1]

class Solution:
    def insertion_sort(self, arr: List[int]):
        for i in range(len(arr)):
            current_index = i

            while current_index > 0 and arr[current_index -1] > arr[current_index]:
                arr[current_index], arr[current_index -1] = arr[current_index -1], arr[current_index]
                current_index -= 1   
    
my_object = Solution()
my_object.insertion_sort(arr)
print(arr)