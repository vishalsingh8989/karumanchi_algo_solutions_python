def getNthUglyNo(n):
 
    ugly = [0]*n
    
    i2 = i3 = i5 = 0
    
    ugly[0] = 1
    
    nm2 = 2
    nm3 = 3
    nm5 = 5
    
    
    for l in xrange(1, n):
        ugly[l] = min(nm2, nm3, nm5)
        
        
        if ugly[l] == nm2:
            i2 += 1
            nm2 = ugly[i2]*2 
        
        if ugly[l] == nm3:
            i3 += 1
            nm3 = ugly[i3]*3 
        
        if ugly[l] == nm5:
            i5 += 1
            nm5 = ugly[i5]*5 
    
    
    print(ugly)
    return ugly[-1]
 
def main():
 
    n = 150
 
    print getNthUglyNo(n)
main()