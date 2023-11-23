# 263. Ugly Number
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.
n = 5
class Solution:
    def isUgly(self, n:int) -> bool:
        if n == 1: return True
        if n % 2 == 0:
            return True
        if n % 3 == 0:
            return True
        if n % 5 == 0:
            return True
        else: return False

obj = Solution()
res = obj.isUgly(n)
print(res)