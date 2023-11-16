class MyCircularQueue:

    def __init__(self, k:int):
        self.size = k
        self.data = [0] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull() == True:
            return False
        if self.isEmpty() == True:
            self.head = 0
        
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = value
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty()  == True:
            return False
        if (self.head == self.tail):
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.size
        return True
    
    def front(self) -> int:
        if self.isEmpty() == True:
            return -1
        return self.data[self.head]
    
    def rear(self) -> int:
        if self.isEmpty() == True:
            return -1
        return self.data[self.tail]
    
    def isEmpty(self) -> bool:
        return self.head == -1
    
    def isFull(self) -> bool:
        return ((self.tail +1) % self.size) == self.head
    

cq = MyCircularQueue(5)


    