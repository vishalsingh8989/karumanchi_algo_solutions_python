""" Add one to a number represented by link list
"""
from linklist import  SimpleNode as Node
from linklist import printlist
import random


import sys

print(sys.version)
print(sys.version_info)
def reverseList(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
 
def getNum(head):
    num = 0   
    curr = head
    while curr is not None:
        num = num*10 + curr.data
        curr = curr.next
    return num
    
    
def addOne(head):    
    num1 = getNum(head)
    head = reverseList(head)
    curr = head
    carry = 1
    prev = None
    while curr is not None:
        sum = carry + curr.data
        carry = 1 if sum >=  10 else 0
        
        sum = sum % 10
        curr.data = sum
        
        prev = curr
        curr = curr.next
    
    if carry >= 1:
        prev.next = Node(carry, None)
        
    head = reverseList(head)
    num2 = getNum(head)
    return num1, num2

def test(num1 , num2):
    return True if num2 == num1 +1 else False
    
if __name__ == "__main__":
    head = None
    res = []
    for i in xrange(3000):
        head = None
        size = random.randint(3,18)
        for i in xrange(size, 0, -1):
            if i == size:
                head = Node(random.randint(1,9), head)
            else:
                head = Node(random.randint(0,9), head) 
            
        num1, num2 = addOne(head)
        truth = test(num1, num2)
        if not truth:
            print(num1, num2)
        res.append(truth)
        
    print("\n%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        
        