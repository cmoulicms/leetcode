from typing import List

arr = [7,3,2,5,6,10,9,8,1]

class Solution:
    def selection_sort(self, arr: List[int]):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i], =  arr[i], arr[min_index],
            
    
my_object = Solution()
my_object.selection_sort(arr)
print(arr)