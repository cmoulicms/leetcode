arr = [1,0,2,3,0,4,5,0]

def duplicate_zeros(arr):
    print()
    for index, value in enumerate(arr):
        if value == 0:
            arr[index+1] = 0


duplicate_zeros(arr)