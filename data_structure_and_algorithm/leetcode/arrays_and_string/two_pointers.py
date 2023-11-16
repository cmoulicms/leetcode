# Two Pointers technique to revers an array


def reverse_array(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


my_array = [2, 4, 5, 8, 9, 3, 0]
reverse_array(my_array)
print(my_array)
