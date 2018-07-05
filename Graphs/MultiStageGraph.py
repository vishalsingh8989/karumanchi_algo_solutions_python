"""
Dynamic programming

"""

import sys
INF = sys.maxint

def findMin(g, u, d):
    
    min_val = sys.maxint
    if u == d:
        print(u,d)
        return g[u][d]
    
    for v in xrange(len(g)):
        if g[u][v]  != INF:
            #print("call " , u, v)
            min_val = min(min_val, g[u][v] + findMin(g, v, d))
    
    print(min_val)
    return min_val
    
    


if __name__ == "__main__":
    
    
    g = [[ INF, 1, 2, 5, INF, INF, INF, INF],
       [INF, INF, INF, INF, 4, 11, INF, INF],
       [INF, INF, INF, INF, 9, 5, 16, INF],
       [INF, INF, INF, INF, INF, INF, 2, INF],
       [INF, INF, INF, INF, INF, INF, INF, 18],
       [INF, INF, INF, INF, INF, INF, INF, 13],
       [INF, INF, INF, INF, INF, INF, INF, 2]]
    
    print(findMin(g, 0,7))
       