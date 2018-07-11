from __future__ import print_function

def printlist(head):
    while head is not None:
        print("( "+str(head.x) + ", " +str(head.y) + " ) ,")
        head = head.next

class Node:
    def __init__(self, x, y, next):
        self.x = x
        self.y = y
        self.next = next

def removeMidPoints(head):
    
    if head is None or head.next is None or head.next.next is None:
        return head
    
    curr  = head
    curr_head = head
    next  = curr.next
    change_x = True if curr.x == next.x else False
    while curr is not None and curr.next is not None:
        if curr.x == next.x and next.x == next.next.x and change_x is True:
            curr = curr.next
        else:
            pass
        
        
    
             
    
    return head

if __name__ == "__main__":
    head = Node(40, 5, None)
    head = Node(20, 5, head)
    head = Node(7, 5, head)
    head = Node(7, 10, head)
    head = Node(5, 10, head)
    head = Node(1, 10, head)
    head = Node(0, 10, head)
    printlist(head)
    