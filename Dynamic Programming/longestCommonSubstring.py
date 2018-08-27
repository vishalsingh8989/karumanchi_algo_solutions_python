

def findMax(str1, str2):
    
    
    
    dp = [[0]*(len(str1) + 1) for i in xrange(len(str2) + 1)]
    result = 0
    
    for i in xrange(len(str2) + 1):
        for j in xrange(len(str1) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0    
    
    return result

if __name__ == "__main__":
    
    
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'
    
    print(findMax(X, Y))
 