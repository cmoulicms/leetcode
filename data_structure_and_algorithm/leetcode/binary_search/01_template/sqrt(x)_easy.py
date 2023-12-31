# Initial Condition: left = 0, right = length-1
# Termination: left > right
# Searching Left: right = mid-1
# Searching Right: left = mid+1

number = 5


class Solution:
    def sqrt(self, x: int) -> int:
        if x < 2:
            return 2

        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot

            if num > x:
                right = pivot - 1

            elif num < x:
                left = pivot + 1

            else:
                return pivot

        return right


myObj = Solution()
print(myObj.sqrt(number))
