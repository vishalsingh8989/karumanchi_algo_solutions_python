def printbits(n, st=""):
    if n==0:
        print(st)
        return 0
    printbits(n-1, st+'0')
    printbits(n-1, st+'1')

printbits(2)
            



