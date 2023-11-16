class MyStack:

    def __init__(self):
        self.data = []
    
    def push(self, value: int):
        self.data.append(value)

    def top(self):
        if self.isEmpty():
            return False
        return self.data[len(self.data) -1]

    def pop(self):
        if self.isEmpty():
            return False
        self.data.pop(len(self.data) -1)
        return True

    def isEmpty(self):
        return len(self.data) == 0
    
s = MyStack()
s.push(1)
s.push(2)
s.push(3)

print(s.top())

s.pop()
print(s.top())

s.pop()
print(s.top())

s.pop()
print(s.top())

print(s.isEmpty())