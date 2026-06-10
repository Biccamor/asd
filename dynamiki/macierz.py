def solve(A):
    n = len(A)
    dp = [[float('inf')]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for L in range(2,n+1):
        for i in range(0,n-L+1):
            j = i+L-1

            for k in range(i,j):
                
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+A[i][0]*A[k][1]*A[j][1])
    return dp[0][n-1]