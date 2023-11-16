from collections import deque
class MovingAverage:

    # Approach 1: Array or List
    # Time complexity: O(n)
    # Space complexity: O(m)
    # def __init__(self,size:int):
    #     self.size = size
    #     self.queue = []

    # def next(self, val:int) -> float:
    #     size, queue = self.size, self.queue
    #     queue.append(val)
    #     window_sum = sum(queue[-size:])

    #     return window_sum / min(len(queue), size)

    # Approach 2: Deque(Double Ended Queue)
    # Time complexity: O(1)
    # Space complexity: O(n)
    def __init__(self, size:int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val:int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val
        return self.window_sum / min(len(self.queue), self.size)

    

    
    
obj = MovingAverage(4)
obj.next(1)
obj.next(3)
obj.next(5)
obj.next(10)
print(obj.next(15))
