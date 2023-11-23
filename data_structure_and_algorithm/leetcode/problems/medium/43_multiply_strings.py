# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

num1 = "2"
num2 = "3"


class Solution:
    def multiply(self, num1: str, num2: str):
        for i in range(len(num1)):
            print(num1[i])

obj = Solution()
res = obj.multiply(num1, num2)
