"""
"""

import sys

def eggDropRec(flr, eggs):
    
    if flr == 0 or flr == 1:
        return flr
    
    if eggs == 1:
        return flr
    
    
    res = sys.maxint
    minval = sys.maxint
    for i in xrange(1, flr+1):
        res = max(eggDropRec(i - 1, eggs - 1), eggDropRec(flr - i, eggs))
                #( egg breaks and below floor or egg dont break check upper flr . return max (worst case)
        minval = min(res, minval)
    
    return minval+1

if __name__ == "__main__":
    eggs = 2
    flr = 10
    print(eggDropRec(flr, eggs))
                
        
    