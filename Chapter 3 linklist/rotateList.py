from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist

def getlength(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count

def rotateRight(head, k):
    if k == 0:
        return head
    
    
    count = 0
    curr = head
    while curr is not None and count + 1 < k :
        curr = curr.next 
        count +=1
    
    new_head = curr.next
    curr.next = None
    
    curr = new_head
    while curr.next is not None:
        curr = curr.next
    
    curr.next = head
    return new_head
  
def rotateLeft(head, k):
    if k == 0:
        return head
    k = getlength(head) - k
    head = rotateRight(head, k)
    
    return head
          
if __name__ == "__main__":
    head = None
    for i in xrange(10, -1,-1 ):
        node = Node(i, head)
        head = node
    printlist(head)
    
    head = rotateRight(head, 3)
    printlist(head)
    
    head = rotateLeft(head, 3)
    printlist(head)
    
    head = rotateLeft(head, 3)
    printlist(head)