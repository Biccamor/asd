def checkRecord(n: int) -> int:
    dp = [[[0 for L in range(3)] for A in range(2)] for _ in range(n+1)]
    
    dp[1][0][0]=1
    dp[1][1][0]=1
    dp[1][0][1]=1
    MOD = 1000000007
    for i in range(2, n+1):
        for j in range(0, 3):
            dp[i][0][0] = (dp[i][0][0] + dp[i-1][0][j])%MOD
        
        for j in range(0,3):
            for k in range(0,2):
                dp[i][1][0] = (dp[i][1][0]+ dp[i-1][k][j])%MOD

        dp[i][0][1] = dp[i-1][0][0]
        dp[i][0][2] = dp[i-1][0][1]

        dp[i][1][1] = dp[i-1][1][0]
        dp[i][1][2] = dp[i-1][1][1]

    ans = 0
    for i in range(0,2):
        for j in range(0,3):
            ans = (ans + dp[n][i][j])%MOD
    return ans 

n=3
print(checkRecord(n))