"""
how many ways can we make the change? The order of coins doesnt matter.
"""
def count(S, n):
 
    table = [0]*(n+1)
    table[0] = 1
    
    for i in S:
        for j in xrange(i, n+1):
            table[j] = table[j] + table[j - i]
        print(table)
        
    return table[n]
    
 


arr = [1,3,5,7]
m = len(arr)
n = 12
print(count(arr,  n))