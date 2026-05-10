def solve(A):
    n = len(A)
    dp = [[0]*3 for _ in range(n)]
    dp[0][1] = -A[0]

    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        dp[i][1] = max(dp[i-1][0]-A[i], dp[i-1][1])
        dp[i][2] = dp[i-1][1]+A[i]
    
    return max(dp[n-1])