# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

accounts = [[-2,-8,-7],[-7,-1,-3],[-1,-9,-5]]
class Solution:

    def maximumWealth(self, accounts) -> int:
        maximumWealth = 0
        for i in range(0,len(accounts)):
            sum = 0
            for j in range(0,len(accounts[0])):
                sum += accounts[i][j]
            if sum > maximumWealth:
                maximumWealth = sum
                sum = 0
        return maximumWealth

obj = Solution()
print(obj.maximumWealth(accounts))