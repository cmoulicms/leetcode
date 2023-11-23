# 599. Minimum Index Sum of Two Lists
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.

# A common string is a string that appeared in both list1 and list2.

# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer in any order.

from typing import List


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

class Solution:
    def findResaurant(self, list1: List[str], list2: List[str]):
        list3 = []
        min_index_sum = 0
        index_sum = 0
        for i in range(0, len(list1)):
            for j in range(0, len(list2)):
                if list1[i] == list2[j]:
                    min_index_sum = i + j
                    list3.append(list1[i])
        return list3


obj = Solution()
res = obj.findResaurant(list1, list2)
print(res)