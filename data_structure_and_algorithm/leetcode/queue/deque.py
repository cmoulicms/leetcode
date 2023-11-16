# Deque : Double Ended Queue

from collections import deque

my_deque = deque()

# Adding element
my_deque.append(4)
my_deque.append(9)
my_deque.append(11)
my_deque.append(3)
my_deque.append(1)
my_deque.append(7)
print(my_deque)

my_deque.appendleft(6)
print(my_deque)

# Removing element
my_deque.pop()
print(my_deque)

my_deque.popleft()
print(my_deque)

# Accessing element
element = my_deque[0]
print(element)

# length of deque
print(len(my_deque))

# checking empty deque
# len(my_deque) == 0 or not my_deque

print( not my_deque)
print(my_deque)
my_deque.rotate(2)
print(my_deque)
my_deque.rotate(-3)
print(my_deque)