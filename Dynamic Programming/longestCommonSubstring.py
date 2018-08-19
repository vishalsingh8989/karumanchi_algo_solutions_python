

def findMax(str1, str2):
    
    dp = [[0]*(len(str1) + 1) for i in xrange(len(str2) + 1)]
    
    result = 0
    for i in xrange(len(str2) + 1):
        for j in xrange(len(str1) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str2[i-1] == str1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0

    return result

if __name__ == "__main__":
    
    
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'
    
    print(findMax(X, Y))
 