"""

     peek()    push()    pop()
-----------------------------------------
Linked List |   O(1)      O(n)      O(1)   <--- we are here in this file
            |
Binary Heap |   O(1)    O(Log n)   O(Log n)  <--- heapify etc
"""


class PQueueNode:
    def __init__(self, data, priority, prev, next):
        self.data = data
        self.priority = priority
        self.prev = prev
        self.next = next

def insert(head, data, priority):
    pass




