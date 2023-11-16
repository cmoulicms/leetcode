
a1 = [1,2,3,4,5]

for i in range(len(a1)-1):
    print(i)

print(id(a1))
a1.append(6)
print(id(a1))

# Iterate through the array elements

#1. Using For loop
for element in a1:
    print(element)

#2. List comprehension
double_array = [ element * 2 for element in a1]
print(double_array)

#3. enumerate the array elements
for index, element in enumerate(a1):
    print("{index}")

# print(len(a1))

#4. While loop
index = 0

while index < len(a1):
    print(a1[index])
    index += 1


# Reverse the array element
#1. Using the list slice, doesn't modify the original array

slice_array = a1[::-1]
print(slice_array)
# print(a1)

#2. Using the reversed function, return the iterator 
reversed_array = reversed(a1)
print(list(reversed_array))

#3. Using the reverse method, modify the original array
a1.reverse()
print(a1)

#List slice
a2 = [3,4,5,6,7,8,9]
array_slice = a2[::-1]
print(array_slice)