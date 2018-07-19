from linklist import DoubleNode as Node, printlist
from random import randint
from linklist import isLinkListSorted


def getLength(head):
    count = 0
    while head is not None:
        count +=1
        head = head.next
    return count


def split(head):
    fast   = head
    slow = head
    while True:
        if fast.next is  None:
            break
        if fast.next.next is  None:
            break
        slow = slow.next
        fast = fast.next.next
    
    temp = slow.next
    temp.prev = None
    slow.next = None
    return temp

def merge(node_a, node_b):
    if node_a is None:
        return node_b
    if node_b is None:
        return node_a

    if node_a.data <= node_b.data:
        head = node_a
        head.next = merge(node_a.next, node_b)
        head.next.prev = head
        head.prev = None
        return head
    else:
        head = node_b
        head.next = merge(node_a, node_b.next)
        head.next.prev = head
        head.prev = None
        return head

def mergesort(head):
    
    if head.next is None:
        return head

    second_half = split(head)
    first_half = head
    node_a = mergesort(first_half)
    node_b = mergesort(second_half)
    
    return merge(node_a, node_b)
    
    
    


if __name__ == "__main__":
    res = []
    head = None    
    for i in xrange(10000):
        size = randint(1, 100)
        head = None
        prev = None
        for i in xrange(size):
            head = Node(randint(1, size*2), prev, head)
            if prev is not None:
                prev.prev = head
            prev = head
        
        head.prev = None
            
        head = mergesort(head)
        res.append(isLinkListSorted(head))
        
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    
        