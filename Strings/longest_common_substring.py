"""
https://en.wikipedia.org/wiki/Longest_common_substring_problem

match  ABAB with BABA

lcs table

          A    B    A    B
     0    0    0    0    0
B    0    0    1    0    1
A    0    1    0    2    0
B    0    0    2    0    3
A    0    1    0    3    0

"""





def findLongCommonSubtring(X,Y):
    """tested on leetcode problem 516 for c++
    """
    sizex = len(X)
    sizey = len(Y)
    LCS = [[0]*(sizey + 1) for x in xrange(sizex+1)]
    LCSVAL = [[""]*(sizey + 1) for x in xrange(sizex+1)]

    result = 0
    for i in xrange(1,sizex + 1):
        for j in xrange(1,sizey + 1):
            
            if X[i-1] == Y[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
                LCSVAL[i][j] = LCSVAL[i-1][j-1] + X[i-1]
            else:
                if LCS[i][j-1] > LCS[i-1][j]:
                    LCS[i][j] = LCS[i][j-1]
                    LCSVAL[i][j] = LCSVAL[i][j-1]
                else:
                    LCS[i][j] = LCS[i-1][j]
                    LCSVAL[i][j] = LCSVAL[i-1][j]
                    
                
    for row in LCS:
        print(row)
    
    for  row in LCSVAL:
        print(row)
    
    return LCS[sizex][sizey]

if __name__ == "__main__":
    X = "bccb"#'OldSite:GeeksforGeeks.org'
    Y = X[::-1]#'NewSite:GeeksQuiz.com' 
    res = findLongCommonSubtring(X, Y)
    print(res)
    
    
    
    
    