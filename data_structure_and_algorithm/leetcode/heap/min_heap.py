# Heap: special type of binary tree.
# 1. Is a complete binary tree.
# 2. value of each node must be no greater than(or no less than) the value of its child node.

# min heap: value in the node no longer greater than its children. Top element has smallest value in the heap.

class MinHeap:

    def __init__(self, heapSize):
        self.heapSize = heapSize

        self.minHeap = [0] * (heapSize + 1)

        self.realSize = 0

    def add(self, element):
        self.realSize += 1

        if self.realSize > self.heapSize:
            self.realSize -= 1
            return
        
        self.minHeap[self.realSize] = element
        pass

    def peek(self):
        return self.minHeap[1]
    
    def pop(self):
        pass

    def size(self):
        return self.realSize

    def __str__(self):
        return str()
    

if __name__ == '__main__':
    minHeap = MinHeap(5)
    print(minHeap.minHeap)