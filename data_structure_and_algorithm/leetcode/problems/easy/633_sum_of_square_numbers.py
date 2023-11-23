# 633. Sum of Square Numbers

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
c = 2
class Solution:
    def judgeSquareSum(self, num: int)-> bool:
        left = 1
        right = num // 2
        if c == 1:
            return True
        while left < right:

            sum = left ** 2 + right ** 2

            if sum == num:
                return True
            elif sum > num:
                right -=1
            else:
                left += 1
        return False
            

obj = Solution()
res = obj.judgeSquareSum(c)
print(res)