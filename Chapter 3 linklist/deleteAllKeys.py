from linklist import DoubleNode as Node, printlist
from random import randint
from mergesortdoublelinklist import mergesort

def delete(node):
    if node.next is not None:
        node.next.prev = node.prev
    
    if node.prev is not None:
        node.prev.next = node.next
    

def deleteAllKeys(head, key):
    
    if head is not None:
        node = head
        while node is not None:
            if node.data == key :
                delete(node)
            node = node.next
                
                
        return head
        
if __name__ == "__main__":
    prev = None
    head = None
    
    for i in xrange(12):
        head = Node(randint(0,8), prev ,  head)
        if prev is not None:
            prev.prev = head
        prev = head
        
    head.prev = None
    
    printlist(head)
    head = deleteAllKeys(head, 4)
    printlist(head)
    
    
    