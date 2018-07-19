
from linklist import SimpleNode as Node
from linklist import printlist

def evenodd(head):
    head1 = Node(-1, None)
    head2 = Node(-1, None)
    h1 = head1
    h2 = head2
    
    while head is not None:
        h1.next = head
        h1 = h1.next
        head = head.next
        if head is not None:
            h2.next = head
            h2 = h2.next
            head = head.next
        
    
    h2.next = None
    
    
    h1.next = head2.next
    return head1.next

if __name__ == "__main__":
    head = None
    for i in xrange(11, 0, -1):
        node = Node(i, head)
        head = node
    
    printlist(head)
    head = evenodd(head)
    printlist(head)
    
    