# my_range = tuple(range(1,10))
# my_string = "string"
# print(type(my_range))
# print(type(my_string))
# for i in my_range: 
#     print(i)

my_list = [1,1,9,1,2,7,3,4,4,4]

# append item to the end of the list.
my_list.append(5)
print(my_list)

# my_list and copied_list are separate but elements are same.
copied_list = my_list.copy()
print(copied_list)

# return number of times item appears in the list
print(my_list.count(1))

# extend list by appending elements from the iterable
my_list.extend([6,7,8])
print(my_list)

# return index of the first occurrence of the item
print(my_list.index(3))

# insert item at the specified index
my_list.insert(1,4)
print(my_list)

# remove item from the specified index and return the list
my_list.pop()
print(my_list)

# remove first occurrence of the item
my_list.remove(7)
print(my_list)

# reverse the order of the items in the list
my_list.reverse()
print(my_list)

# sort list in ascending order
my_list.sort()
print(my_list)


