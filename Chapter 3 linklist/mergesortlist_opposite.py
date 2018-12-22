from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist
import random, time


def issorted(head):
    if head is None:
        return True
    prev = head.data
    head = head.next
    while head:
        if head.data < prev:
            return False
        prev = head.data
        head = head.next
    return True


def gethalf(head):
    
    fastptr = head
    slowptr = head
    while fastptr and fastptr.next:
        fastptr = fastptr.next.next
        if fastptr is None:
            break
        slowptr = slowptr.next
    return slowptr    

    

def getLength(head):
    count = 0
    while head is not None:
        head = head.next
        count +=1
    return count

def merge(node_a, node_b):
    if node_a is None:
        return node_b
    if node_b is None:
        return node_a
    
    if node_a.data <  node_b.data:
        head = node_a
        node_a.next = merge(node_a.next, node_b)
        return head
    else:
        head = node_b
        node_b.next = merge(node_a, node_b.next)
        return head


def mergesort(head):
    #mid = getLength(head)/2
    if head is None or head.next is None:
        return head

#     first_half = head
#     while mid - 1 > 0:
#         mid -= 1
#         first_half = first_half.next
#     
#     
#     second_half = first_half.next
#     first_half.next = None
#     
#     first_half = head

    node  = gethalf(head)
    
    second_half = node.next
    #print(head.data,second_half.data )
    #time.sleep(1)
    node.next = None
    first_half = head
    
    node_a = mergesort(first_half)
    
    node_b = mergesort(second_half)
    
    return merge(node_a, node_b)
    
    


if __name__ == "__main__":
    
    res = []
    
    for x in xrange(1000):
        size = random.randint(1,100)
        head = Node(random.randint(1,100), None)
        for i in xrange(1,size):
            node = Node(random.randint(1,100), head)
            head = node
    
    
    
    #printlist(head)
        head = mergesort(head)
        res.append(issorted(head))
    print("{} pass".format(res.count(True)))
    print("{} fail".format(res.count(False)))
    
    