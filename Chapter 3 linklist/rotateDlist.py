from linklist import DoubleNode as Node, printlist
from random import randint
from linklist import isLinkListSorted



def rotateDlist(head, k):
    
    if k == 0:
        return head
    
    c = 1
    curr = head
    
    while curr is not None and c < k:
        curr = curr.next
        c +=1
    
    
    if curr is None:
        return head
    else:
        tail = curr
        while tail.next is not None:
            tail = tail.next
        
        tail.next = head
        head.prev = tail

        head = curr.next
        curr.next = None
        head.prev = None
        
        return head
        
        
        
        





if __name__ == "__main__":
    prev = None
    head = None
    
    for i in xrange(2):
        print("***********************************")
        size  = randint(4,10)
        head = None
        for i in xrange(size):
            head = Node(i, prev, head)
            if prev is not None:
                prev.prev = head
            prev = head
        
        head.prev = None
        printlist(head)
        head = rotateDlist(head,3)
        printlist(head)