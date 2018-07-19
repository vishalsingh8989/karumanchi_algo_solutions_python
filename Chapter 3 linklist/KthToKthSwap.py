"""https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/
"""
from linklist import SimpleNode as Node, printlist


def swapKth(head, k):
    kthone  = head
    i = 0
    while i < k - 1 and kthone is not None:
        kthone = kthone.next
        i +=1
    
    
    kthtwo  = head
    i = 0
    while i < k  and kthtwo is not None:
        kthtwo = kthtwo.next
        i +=1
    
    runner = kthtwo
    kthtwo = head
    while runner is not None:
        runner = runner.next 
        kthtwo = kthtwo.next
    
    kthone.data, kthtwo.data = kthtwo.data, kthone.data
    return head
    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    
    head = None
    nums  = [1, 2, 3, 4, 5, 6, 7, 8 ]
    nums.reverse()

    for i in xrange(len(nums)):
        head = Node(nums[i], head)
    printlist(head)
    head = swapKth(head, 1)
    printlist(head)
    head = swapKth(head, 2)
    printlist(head)
    