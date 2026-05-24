def solve(M: list[tuple]): 
    n = len(M)
    dp = [[int(float('inf'))]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0


    for L in range(2, n+1):
        for i in range(n - L + 1):

            j = L + i - 1 

            for k in range(i, j): 
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + M[i][0]*M[k-1][0]*M[j][1])

    return dp[0][n-1]