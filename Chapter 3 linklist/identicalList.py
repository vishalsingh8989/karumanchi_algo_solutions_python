from __future__ import print_function
from linklist import SimpleNode as Node
from linklist import printlist
from random import randint


def isIdenticalRec(one, two):
    if one is None and two is None:
        return True
    if one is not None and two is not None:
        return one.data == two.data and isIdenticalRec(one.next, two.next)
    
    return False
    

def isIdenticalItr(one, two):
    
    while one is not None and two is not None:
        if one.data != two.data:
            return False
        
        one = one.next
        two = two.next
    return  one is None and two is None

if __name__ == "__main__":
    head_one = Node(0, None)
    for i in xrange(1,10):
        node = Node(i, head_one)
        head_one = node
    
    head_two = Node(0, None)
    for i in xrange(1,10):
        node = Node(i, head_two)
        head_two = node
    
    head_three = Node(0, None)
    for i in xrange(1,5):
        node = Node(i, head_three)
        head_three = node
    for i in xrange(1,5):
        node = Node(randint(1,100), head_three)
        head_three = node
    
    printlist(head_one)
    printlist(head_two)
    
    print("\nIs identical Itr, ", isIdenticalItr(head_one, head_two))
    print("\nIs identical Rec, ", isIdenticalRec(head_one, head_two))
    
    print("\nIs identical Itr, ", isIdenticalItr(head_one, head_three))
    print("\nIs identical Rec, ", isIdenticalRec(head_one, head_three))
    