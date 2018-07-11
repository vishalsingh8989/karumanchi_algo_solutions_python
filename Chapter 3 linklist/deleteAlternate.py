from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist


def deleteAlternate(head):
    curr = head
    while curr is not None:
        node = curr.next
        if node is not None:
            curr.next = node.next
            del node
        curr = curr.next
    return head

if __name__ == "__main__":
    head = None
    for i in xrange(20, -1,-1 ):
        node = Node(i, head)
        head = node
    printlist(head)
    head = deleteAlternate(head)
    printlist(head)
    