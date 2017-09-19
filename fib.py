printed = []

def fib(n):
    
    if n<2:
        if n not in printed:
                printed.append(n)
                print(n)
        return n
    else:
        num = fib(n-2) + fib(n-1)
        if n not in printed:
            print(num)
            printed.append(n)
        return num


print(fib(10))
print(len(printed))
