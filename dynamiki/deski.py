def solve(C,B,s):
    n = len(B)
    m = len(B[0])

    dp = [[float('inf') for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if B[i][j] > s: 
                return -1

    dp[n-1][m-1] = 0 

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i==n-1 and j == m-1: continue

            if min(n-i, m-j) == 1 and C[i][j] <= s: 
                dp[i][j] = 0
                continue


            ans = float('inf')

            if i+1 < n and C[i][j] - C[i+1][j] <= s: # ciecie w dol
                ans = min(ans, dp[i+1][j] + 1)
            
            elif i>= n:
                ans = min(ans, dp[i][j+1]+1)

            if j+1 < m and C[i][j] - C[i][j+1] <= s: 
                ans = min(ans,dp[i][j+1] + 1)
            
            elif j>=m:
                ans = min(ans, dp[i+1][j]+1)
            
            dp[i][j] = ans
    print(dp)
    return dp[0][0]

B = [(2, 1, 4),
(1, 3, 1),
(2, 3, 3)]
C = [(20, 15, 8),
(13, 10, 4),
( 8, 6, 3)]
s = 5

print(solve(C,B,s))