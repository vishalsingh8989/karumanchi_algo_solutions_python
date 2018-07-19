"""
The sieve of Eratosthenes is one of the most efficient ways to find all
primes smaller than n when n is smaller than 10 million
"""

def SieveOfEratosthenes(n):
    
    primes = [False]*n
    p = 2
    
    while p*p <=n :
        
        if primes[p] == False:
            for i in xrange(2*p , n, p):
                primes[i] = True
        
        p += 1
    
    return [i for i in xrange(n) if primes[i] is False]

if __name__ == "__main__":
    print(SieveOfEratosthenes(100))
    
    