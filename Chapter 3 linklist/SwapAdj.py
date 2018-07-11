from __future__ import print_function
from linklist import SimpleNode

def printlist(head):
    print("Link list :" ,end = " : ")
    while head is not None:
        print(head.data, end = " -> ")
        head = head.next

def SwapAdj(head):
    curr  = head  
    if curr is not None and curr.next is not None:
        next  = curr.next 
        new_head = next.next
        next.next = curr
        curr.next = SwapAdj(new_head)
        return next
    return head
        
        
         
    
        
if __name__=="__main__":
    prev = SimpleNode(0, None)
    for i in xrange(1,11):
        node = SimpleNode(i, prev)
        prev = node
    
    head = prev
    printlist(head)
    
    head = SwapAdj(head)
    print()
    printlist(head)