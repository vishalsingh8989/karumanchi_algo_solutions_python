char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
start = [0,10,61,45,30,60]
tinyUrlmap = {}
print(len(char))
def generate():
    carry = 1
    for i in xrange(5, -1, -1):
        start[i] = start[i] + carry
        if start[i]  == len(char):
            start[i] = 0
            carry = 1
        else:
            break
    
    print(start)
    res = "".join([char[i] for i in start])
    return res
    
for i in xrange(500):
    
    print(generate())