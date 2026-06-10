def solve(B,C,s):
    n = len(B)
    m = len(B[0])
    dp = [[float('inf')]*m for _ in range(n)]
    dp[n-1][m-1] = 0 

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):

            if (n-i == 1 or m-j == 1) and C[i][j] <= s:
                dp[i][j] = 0 
                continue

            if j+1 < m and C[i][j]-C[i][j+1] <= s:
                dp[i][j] = min(dp[i][j+1]+1, dp[i][j])
            
            if i+1 < n and C[i][j]-C[i+1][j] <= s:
                dp[i][j] = min(dp[i+1][j]+1, dp[i][j])
    
    return dp[0][0] if dp[0][0]!=float('inf') else -1



B = [(2, 1, 4),
(1, 3, 1),
(2, 3, 3)]

C = [(20, 15, 8),
(13, 10, 4),
( 8, 6, 3)]

s=5

print(solve(B,C,s))