# 1. Compare function
name = "Chandramouli"
name2 = "Chandramouli"
print(id(name))
print(id(name2))

# 2. Immutable and mutable

name = "Hello"
print(id(str))
name2 = "world" + name
print(str)

# 3. Extra operations
# concatenate
# find
# print(str.index("H"))

# substring
# print(str[:4])

# Immutable String: Problems and Solutions
s = ""
n = 5
for i in range(n):
    s += "hello"
    print(id(s))
print(s)

# convert string literal to list

str_to_list = "chan"
characters = list(str_to_list)
for i in range(len(characters)):
    characters.append(characters[i])
print(characters)

print(str_to_list[::-1])
