# 1492. The kth Factor of n
# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
n = 12
k = 3
class Solution:

    def kthFactor(self, n: int, k:int):
        factor = []
        for i in range(1,n+1):
            if n % i == 0:
                factor.append(i)
        if k <= len(factor):
            return factor[k-1]
        else:
            return -1
            

obj = Solution()
res = obj.kthFactor(n,k)
print(res)