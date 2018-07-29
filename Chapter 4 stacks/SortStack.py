""" Only three operations are premitted.
push, pop, top
"""

import random
from test import isSorted

def sortedInsert(stack, element):
    if not stack or stack[-1] <  element:
        stack.append(element)
    else:
        temp = stack.pop()
        sortedInsert(stack, element)
        stack.append(temp)

def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        sortedInsert(stack, temp)



if __name__ == "__main__":
    res = []
    for i in xrange(1001):
        size = random.randint(10,100)
        stack = [random.randint(0, 500) for _ in xrange(size)]
        sortStack(stack)
        res.append(isSorted(stack))
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    
        