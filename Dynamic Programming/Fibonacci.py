def FibItr(n):
    if n <  0:
         print("Invalid Input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a = 0
    b = 1
    for i in xrange(1,n):
        c = a + b
        a = b 
        b = c
    return c

if __name__ == "__main__":
    print(FibItr(10))