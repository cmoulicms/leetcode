# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

text_list = ["H", "e", "l", "l", "o"]

class Solution:
    def reverse_string(self,s):

        # Approach 1: Two pointers, iteration, O(1) space
        # O(N) space to swap N/2 elements
        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        
        # Approach 2: Recursion
        # Time complexity : O(N) time to perform N/2 swaps.
        # Space complexity : O(N) to keep the recursion stack.
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
        
        helper(0, len(s)-1)

obj = Solution()
res = obj.reverse_string(text_list)
print(text_list)
