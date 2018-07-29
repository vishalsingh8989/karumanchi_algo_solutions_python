"""
"""

def reverseWords(line = ""):
    stack = []
    
    res = ""
    for i in xrange(len(line)):
        if line[i] == ' ':
            while stack:
                res = res + stack.pop()
            res = res + " "
        else:
            stack.append(line[i])
            
    while stack:
        res = res + stack.pop()
    
    return res        
            

if __name__ == "__main__":
    line = "Geeks for Geeks"
    print(reverseWords(line))
    line = "Hello World"
    print(reverseWords(line))
    