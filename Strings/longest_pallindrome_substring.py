"""Complexity O(n^2)
"""

def findlonPallindrome(word):

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
    #word = "ababababcbcbcbc"
    find(word)
    longestPalSubstr(word)
    
    
