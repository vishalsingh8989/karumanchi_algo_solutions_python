
import random

def numberToWords(num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n/10-2]] + words(n%10)
        if n < 1000:
            return [to19[n/100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion', 'Trillion'), 1):
            if n < 1000**(p+1):
                return words(n/1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'


def convertTonum(words):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    
    words = words.split()
    values = {i:k for k, i in enumerate(to19,1)}
    for idx, val in enumerate(tens,2):
        values[val] = idx*10
    values['Hundred'] = 100
    total = 0
    
    
    currnum = 0
    for w in words:
        if w == "Trillion":
            total += currnum *(10**12)
            currnum = 0
        elif w == "Billion":
            total += currnum *(10**9)
            currnum = 0
        elif w == "Million":
            total += currnum *(10**6)
            currnum = 0
        elif w == "Thousand":
            total += currnum *(10**3)
            currnum = 0
        elif w == "Hundred":
            currnum =  currnum*100
        else:
            currnum +=  values[w]
    total += currnum
    return total
        
            
    
        
    
    
    
    

num = 10
p = 9

res = []

for i in xrange(1, 100000):
    limit = num**p
     
    n = random.randint(1, limit)
 
    words = numberToWords(n)
     
    p = (p + 1)%17
    total = convertTonum(words)
     
    #print(n, words )
    if n != total:
        print(n, words , "fail")
    res.append(n == total)




print("{} pass".format(res.count(True)))
print("{} fail".format(res.count(False)))

