from typing import List

arr = [7,3,2,5,6,10,9,8,1]

class Solution:
    def bubble_sort(self, arr: List[int]):
        has_swapped  = True
        while has_swapped:
            has_swapped = False
            for i in range(len(arr)-1):
                next = i + 1
                if arr[i] > arr[next]:
                    arr[i], arr[next] = arr[next], arr[i]   
                    has_swapped = True         
    
my_object = Solution()
my_object.bubble_sort(arr)
print(arr)