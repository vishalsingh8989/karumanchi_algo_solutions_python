from linklist import DoubleNode as Node, printlist
from random import randint
from linklist import isLinkListSorted
import time

def insertionSort(head):
   
    if head is None:
        return None
    start = head
    next = head.next
    
    while next is not None:
        
        node = next
        next = node.next        
        key = node.data
        curr = node.prev
        
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        
        while curr is not None and curr.data >  key:
            curr = curr.prev
        
        if curr is None:
            node.next = head
            head.prev = node
            node.prev = None
            head = node
        else:
            node.next = curr.next
            node.prev = curr
            curr.next = node
            if node.next is not None:
                node.next.prev = node
        
        
    return head
        
            

if __name__ == "__main__":

    res = []
    for i in xrange(100000):
        prev = None
        head = None
        size = randint(1,100)
        for i in xrange(size):
            head = Node(randint(1, 100), prev, head)
            if prev is not None:
                prev.prev = head
            prev = head
        
        if head is not None:
            head.prev = None
        
        #printlist(head)
        head = insertionSort(head)
        #printlist(head)
        #print("isLinkListSorted" , isLinkListSorted(head))
        res.append(isLinkListSorted(head))
    
    print("%s  Pass."%(res.count(True)))
    print("%s  Fail."%(res.count(False)))
