from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist

def printReverse(head):
    if head is None:
        return 
    printReverse(head.next)
    print(head.data , end ="->")

if __name__ == "__main__":
    
    head = Node(0, None)
    for i in xrange(1,10):
        node = Node(i, head)
        head = node
    printlist(head)
    print("Reverse list : ")
    printReverse(head)
    
    
    