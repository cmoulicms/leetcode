class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head

        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    # O(1) constant time
    def addAtHead(self, val: int):
        self.addAtIndex(0, val)

    # O(n) linear time
    def addAtTail(self, val: int):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int):
        if index > self.size:
            return

    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            return
        self.size = self.size - 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next


obj = MyLinkedList()
param1 = obj.get(1)
print(param1)
# obj.addAtHead(3)
# obj.addAtTail(5)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
