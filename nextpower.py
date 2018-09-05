

def nextp(n):
    v = 1
    
    while v < n:
        v = v << 1
    
    return v


for i in xrange(33):
    print(i ,  nextp(i))
    