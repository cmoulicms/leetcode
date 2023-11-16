nums = [1,2,3,4,5,6,7]

def prefix_sum(nums):
    n = len(nums)
    total = 0
    for i in range(n):
        total = nums[i] + total
        nums[i] = total

prefix_sum(nums)
print(nums)