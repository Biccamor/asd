def solve(M):
    n = len(M)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)

    return dp[n-1][n-1]