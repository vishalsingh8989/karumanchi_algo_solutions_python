import time

print(__name__)

class Memosize(object):
    def __init__(self, fn):
        self.fn = fn
        self.mem = {}
    
    def __call__(self, X):
        if X not in self.mem:
            self.mem[X] = self.fn(X)
        return self.mem[X]

def memosize(f):
    mem = {}
    def helper(x):
        if x not in mem:
            mem[x] = f(x)
        return mem[x]
    return helper

@Memosize
def fib(x):
    if x == 0 or x == 1:
        return x
    else:
        return fib(x-1) + fib(x-2)

if __name__ == "__main__":
    start = time.time()
    print("start")
    print("Val : ",fib(38))
    print("Time taken :  " , (time.time()-start))
    