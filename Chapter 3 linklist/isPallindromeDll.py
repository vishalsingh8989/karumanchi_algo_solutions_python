from linklist import DoubleNode as Node, printlist
from random import randint
from linklist import isLinkListSorted



def isPallindrome(head):
    if head is None:
        return True
    
    tail = head
    while tail.next is not None:
        tail = tail.next
    
    while head != tail :
        if head.data != tail.data:
            return False
        head = head.next 
        tail = tail.prev
    
    return True
        
if __name__ == "__main__":
    head = None
    prev = None
   
    res = []
    alp = {
        "level" :True,
        "leel"  :True, 
        "Hello" :False, 
        "lallal" :True,
        "Anna" :  False,
        "Jazz" :  False
                }
    for key, val in alp.iteritems():
        #print(key ,  val)
        head = prev = None
        for i in xrange(len(key)):
            head = Node(key[i] , prev ,  head)
            if prev is not None:
                prev.prev = head        
            prev = head
            
        head.prev = None
        
        #printlist(head)
        if val is isPallindrome(head):
            res.append(True)
        else:
            res.append(False)
        #res.append(val is isPallindrome(head))
    print("%s  Pass."%(res.count(True)))
    print("%s  Fail."%(res.count(False)))
    
    
    