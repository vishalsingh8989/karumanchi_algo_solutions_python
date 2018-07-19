""" Add one to a number represented by link list
"""
from linklist import  SimpleNode as Node
from linklist import printlist
import random

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
    while curr is not None:
        curr.data = curr.data + 1
        if curr.data == 10:
            curr.data = 0
            curr = curr.next
        else:
            break
    head = reverseList(head)
    num2 = getNum(head)
    print(num1, num2)
    return True if num2  ==  num1 + 1 else False
    
if __name__ == "__main__":
    head = None
    res = []
    for i in xrange(300):
        head = None
        size = random.randint(3,9)
        for i in xrange(size, 0, -1):
            if i == size:
                head = Node(random.randint(1,9), head)
            else:
                head = Node(random.randint(0,9), head) 
            
        #printlist(head)
        res.append(addOne(head))
        
    print("\n%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        
        