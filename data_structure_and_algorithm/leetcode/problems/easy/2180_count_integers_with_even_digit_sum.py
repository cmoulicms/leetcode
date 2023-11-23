# 2180. Count Integers With Even Digit Sum
# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

# The digit sum of a positive integer is the sum of all its digits.
num = -1
class Solution:
    def countEven(self, num:int) -> int: 
        even_digit_sum = 0
        digit_sum = 0
        for i in range(1,num+1):
            while i > 0:
                digit_sum += i % 10 
                i //= 10
            if digit_sum % 2 == 0:
                even_digit_sum += 1
            else:
                digit_sum = 0
        return even_digit_sum

            

obj = Solution()
res = obj.countEven(num)
print(res)