

def editDistanceRec(str1, str2, m, n):
    if n == 0:
        return m
    
    if m == 0:
        return n
    
    if str1[m-1] == str2[n-1]:
        return editDistanceRec(str1, str2, m-1, n-1)

    return 1 + min(editDistanceRec(str1, str2, m-1, n), editDistanceRec(str1, str2, m, n-1), editDistanceRec(str1, str2, m-1, n-1))



def editDistanceDp(str1, str2):
    """
    O(mn)
    """
    dp = [[0] * (len(str1) + 1) for _ in xrange(len(str2) + 1)]
     
    
    for i in xrange(len(str2)+1):
        for j in xrange(len(str1)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    
    for row in dp:
        print(row)
    
    return dp[-1][-1]

if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    print editDistanceRec(str1, str2, len(str1), len(str2))
    print editDistanceDp(str1, str2)
    
    
    
    
    