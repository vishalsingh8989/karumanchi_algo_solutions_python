from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist


def reverseKNode(head, k ):
    count = 0
    curr = head
    prev = None
    
    while count < k and curr is not None:
        next = curr.next 
        curr.next = prev
        prev = curr
        curr = next
        count +=1
    
    if curr is not None:
        temp = reverseKNode(curr, k)
        head.next = temp
    
    return prev

if __name__ == "__main__":
    head = None
    for i in xrange(22, -1,-1 ):
        node = Node(i, head)
        head = node
    printlist(head)
    
    head = reverseKNode(head, 5)
    printlist(head)
    