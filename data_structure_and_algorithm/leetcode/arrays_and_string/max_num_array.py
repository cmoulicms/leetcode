import datetime
#1. Iterative approach

iterative_array = list(range(1,100000000))

max_num = iterative_array[0]
print("Iterative approach")
print(f"Start ----------------> {datetime.datetime.now().time()}")
for element in iterative_array:
    if element > max_num:
        max_num = element
print(f"End ----------------> {datetime.datetime.now().time()}")

#2. Using max() function

max_function_array = list(range(1,100000000))
print("Using max() function")
print(f"Start ----------------> {datetime.datetime.now().time()}")
max(max_function_array)
print(f"End ----------------> {datetime.datetime.now().time()}")

#3. Sorting 

sorted_array = list(range(1,100000000))
print("Using Sorting technique")
print(f"Start ----------------> {datetime.datetime.now().time()}")
sorted_array[len(sorted_array)-1]
print(f"End ----------------> {datetime.datetime.now().time()}")

#4. Divide and Conqure


