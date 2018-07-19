"""
"""
from linklist import SimpleNode as Node
from linklist import printlist
import time
import random

def test(head):
    while head is not None and head.next is not None:
        if head.data >  head.next.data:
            return False
        head = head.next
    return True
    

def insertionSort(head):
    if head is not None:
        root = Node(head.data, None)
        curr = root
        head = head.next
        
    while head is not None:
        prev = None
        curr = root
        if head.data < root.data:
            node = Node(head.data, root)
            root = node
            head = head.next
            continue
        while curr.next is not None and curr.next.data <  head.data:
            prev = curr
            curr = curr.next

        node = Node(head.data, curr.next)
        curr.next = node
        head = head.next
    return root

def mklist(initializer):
    head = temp = Node(initializer[0], None)
    for i in xrange(1, len(nums)):
        n = Node(initializer[i], None)
        temp.next = n
        temp = temp.next
    return head


if __name__ == "__main__":

    res = []
    start = time.time()
    for _ in xrange(1000):
        size = random.randint(8,100)
        nums = [random.randint(1,2000) for _ in xrange(size)]
        root = mklist(nums)
        #printlist(root)
        root =  insertionSort(root)
        #printlist(root)
        res.append(test(root))
     
     
    end = time.time()
    print("\n%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))



     
    