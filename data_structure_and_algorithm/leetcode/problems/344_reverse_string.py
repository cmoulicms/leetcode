text_list = ["H", "e", "l", "l", "o"]


def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


reverse_string(text_list)
print(text_list)