
import math

def maxReverals(string = ""):
    
    
    if len(string)%2 != 0 :
        return -1
    
    stack = []
    for i in xrange(len(string)):
        
        if string[i] == "{":
            stack.append(string[i])
        else:
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(string[i])
    
    
    print(stack)

    b_open = stack.count("{")
    b_close = stack.count("}")
        
    return int((b_open+1)/2 + (b_close+1)/2)
        



if __name__ == "__main__":
    
    
    experssion = {"}{":2,
                  "{{{":-1,
                  "{{{{":2,
                  "{{{{}}":1,
                  "}{{}}{{{":3
                  }

    res = []
    for key, val in experssion.iteritems():
        maxRev = maxReverals(key)
        print(key, maxRev, val)
        res.append(maxRev == val)
    
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
        
    
    