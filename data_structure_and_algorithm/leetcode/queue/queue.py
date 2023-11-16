# Queue Implementation

class MyQueue:
    def __init__(self):
        self.data = []
        self.q_start = 0
    
    def enQueue(self,x):
        self.data.append(x)
        return True
    
    def deQueue(self):
        if self.isEmpty() == True:
            return False
        self.q_start += 1
        return True
        
    
    def front(self):
        return self.data[self.q_start]
    
    def isEmpty(self)-> bool:
        return self.q_start >= len(self.data)
    
q = MyQueue()

q.enQueue(5)
q.enQueue(10)

if q.isEmpty() == False:
    print(q.front())

q.deQueue()
if q.isEmpty() == False:
    print(q.front())

q.deQueue()
if q.isEmpty() == False:
    print(q.front())
else:
    print('Queue is empty')

