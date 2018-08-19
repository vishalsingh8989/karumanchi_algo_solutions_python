"""

Example : num = \"1234\"
sumofdigit[0] = 1 = 1
sumofdigit[1] = 2 + 12  = 14
sumofdigit[2] = 3 + 23  + 123 = 149
sumofdigit[3] = 4 + 34  + 234 + 1234  = 1506
Result = 1670


Solution: 

For above example,
sumofdigit[3] = 4 + 34 + 234 + 1234
           = 4 + 30 + 4 + 230 + 4 + 1230 + 4
           = 4*4 + 10*(3 + 23 +123)
           = 4*4 + 10*(sumofdigit[2])
In general, 
sumofdigit[i]  =  (i+1)*num[i] + 10*sumofdigit[i-1]

"""

def findSum(string):
    
    result = int(string[0])
    
    sumdigits = [0]*(len(string))
    sumdigits[0] = int(string[0])
    
    for i in xrange(1,len(string)):
        
        sumdigits[i] = (i+1)*int(string[i]) + 10*sumdigits[i-1]
    
        result += sumdigits[i]
        
    return result

        

if __name__ == "__main__":
    print(findSum("1234"))
    
    
    
    