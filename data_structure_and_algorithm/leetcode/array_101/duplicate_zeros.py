remove_duplicate = [1,5,0,4,0,3,9]

# for index, i in enumerate(remove_duplicate):
#     if(i == 0):
#         remove_duplicate[index] = 0

# print(remove_duplicate)
i = 0
while i < len(remove_duplicate):
    if(remove_duplicate[i] == 0):
        remove_duplicate[i+1] = 0
    i += 1


print(remove_duplicate)

        

