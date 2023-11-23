# 367. Valid Perfect Square

# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.
num = 9


class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        # Time Limit Exceeded when num = 2000105819 for below code.
        # n = num // 2
        # if num == 1:
        #     return True
        # for i in range(0, n):
        #     if i ** 2 == num:
        #         return True
        # return False

        # binary search method
        left = 0
        right = num // 2
        if num == 1:
            return True
        while left <= right:
            mid = (left + right) // 2

            if num == mid ** 2:
                return True
            elif num > mid ** 2:
                left = mid + 1
            else:
                right = mid -1
        return False


obj = Solution()
res = obj.isPerfectSquare(num)
print(res)
