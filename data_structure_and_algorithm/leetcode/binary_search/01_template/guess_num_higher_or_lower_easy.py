import guess

number = 12


class Solution:
    def guessNumber(self, num):
        low, high = 0, num
        while low <= high:
            mid = low + (high - low) / 2
            res = guess(mid)

            if res == mid:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1
        return -1


myObj = Solution()
print(myObj.guessNumber(number))
