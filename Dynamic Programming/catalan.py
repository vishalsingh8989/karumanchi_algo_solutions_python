"""

Or use T(n) = (2n)! / (n+1)!n! # geeksforgeeks


and Labelled trees

Number of Labeled Tees = (Number of unlabeled trees) * n!
                       = [(2n)! / (n+1)!n!]  × n!
"""
def catalonRec(n):
    if n <= 1:
        return 1
    
    res = 0
    for i in xrange(n):
        res += catalonRec(i) * catalonRec(n - i - 1)
    
    return res


def catalanDP(n):
    
    if n == 0 or n == 1:
        return 1
    
    catalan = [0]*(n+1)
    
    catalan[0] = 1
    catalan[1] = 1
    
    for i in xrange(2, n+1):
        for j in xrange(i):
            catalan[i] = catalan[i] + catalan[j]*catalan[i-j-1]
    
    return catalan[n]
            

if __name__ == "__main__":
    for i in xrange(10):
        print(catalonRec(i))
    
    for i in xrange(10):
        print(catalanDP(i))