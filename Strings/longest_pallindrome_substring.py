"""Complexity O(n^2)
"""



def findLongPallindromeOpt(word):
    """Complexity O(n^2)
    """
    wordone = word
    wordtwo = word[::-1]
    #print(wordone)
    #print(wordtwo)
    
    sizex = len(word)
    sizey = len(word)
    table = [[0] * (sizex + 1) for _ in xrange(sizey + 1)]
    
    max_length = 1
    end_idx = 1
    for i in xrange(1, sizex):
        for j in xrange(1, sizey):
            if wordtwo[i] == wordone[j]:
                table[i][j] = table[i-1][j-1] + 1 
                if table[i][j] >  max_length:
                    max_length = table[i][j]
                    end_idx = i 
    for row in table:
        print(row)
    return word[end_idx - max_length :end_idx ]

def findlonPallindrome(word):
    """Complexity O(n^2)
    """
    table = [[False]*len(word) for x in xrange(len(word))]

    #for x in xrange(len(word)):
    #    print(table[x])

    for x in xrange(len(word)):
        table[x][x] = True

    maxlength = 1
    start_idx = 0  

    for x in xrange(len(word) - 1):
        if word[x] == word[x+1]:
            table[x][x+1] = True
            start_idx = x
            maxlength = 2
    

    for k in xrange(3, len(word)+1):
        for i in xrange(len(word) - k + 1):
            j = i + k - 1
            #print(i,j)
            if word[i] == word[j]  and table[i+1][j-1] :
                table[i][j] = True
                #table[j][i] = True
                if k >  maxlength:
                    maxlength = k
                    start_idx = i
                    print(start_idx, maxlength)

    #print(start_idx, maxlength)
    return word[start_idx:start_idx + maxlength ]


    
if __name__ == "__main__":
    word = "forgeeksskeegfor"
    #find(word)
    word = "ababababcbcbcbc"
    word = "aa"
    word = "babcbabcbaccba"
    pallin = findlonPallindrome(word)
    print(pallin)
    pallin = findLongPallindromeOpt(word)
    print(pallin)
    
    
