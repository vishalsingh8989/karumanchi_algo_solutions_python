from linklist import DoubleNode as Node, printlist
from random import randint
from linklist import isLinkListSorted


def insert(head, data):
    
    if head is None:
        head = Node(data, None, None)
        return head
    
    if head.data >= data:
        node = Node(data, None, head)
        head.prev = node
        head = node
        return head
    
    start = head
    while start.next is not None and start.next.data  < data:
        start = start.next 
    
    if start.next is not None:
        node = Node(data, start, start.next)
        start.next = node
        node.next.prev = node
    else:
        node = Node(data, start, None)
        start.next = node
    return head


def deleteNth(head, n):
    
    if n == 1:
        head = head.next 
        head.prev = None
        return head
    
    start = head
    k = 0
    while start is not None and k < n:
        k +=1
        start = start.next

if __name__ == "__main__":
    
    prev = None
    head = None
    
    for i in xrange(30, 10, -3):
        head = Node(i, prev, head)
        if prev is not None:
            prev.prev = head
        prev = head
        
        head.prev = None
    printlist(head)

    head = insert(head, 13)
    printlist(head)
    head = insert(head, 11)
    printlist(head)
    head = insert(head, 31)
    printlist(head)
    head = deleteNth(head, 1)
    printlist(head)