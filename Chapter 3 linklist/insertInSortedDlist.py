from linklist import DoubleNode as Node, printlist
from random import randint
from linklist import isLinkListSorted
from platform import node


def insert(head, data):
    
    if head is None:
        head = Node(data, None, None)
        return head
    
    if head.data >= data:
        node = Node(data, None, head)
        head.prev = node
        return node
    
    start = head
    while start.next is not None and start.next.data < data:
        start = start.next
    
    if start.next is None:
        start.next = Node(data, start, None)
        return head
    else:
        node = Node(data, start, start.next)
        start.next = node
        node.next.prev = node
        return head
        


def deleteNth(head, n):
    
    if n == 1 :
        head = head.next
        head.prev = None
        return head
    
    node = head
    k = 0
    while node is not None and k < n -1:
        k +=1
        node = node.next
    
    
    if node is None:
        return head
    
    if node.next is not None:
        node.next.prev = node.prev
        
    if node.prev is not None:
        node.prev.next = node.next
        
    return head

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
    print("isLinkListSorted : " , isLinkListSorted(head))
    head = deleteNth(head, 1)
    printlist(head)
    head = deleteNth(head, 2)
    printlist(head)
    print("isLinkListSorted : " , isLinkListSorted(head))
    head = deleteNth(head, 8)
    printlist(head)
    print("isLinkListSorted : " , isLinkListSorted(head))
    head = deleteNth(head, 8)
    printlist(head)
    head = deleteNth(head, 7)
    printlist(head)
    print("isLinkListSorted : " , isLinkListSorted(head))
    head = deleteNth(head, 4)
    printlist(head)
    
    print("isLinkListSorted : " , isLinkListSorted(head))