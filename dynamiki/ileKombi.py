def solve(n):
    dp =[0]*(n+1) 
    dp[0] = 1
    for i in range(1,n+1):
        for k in range(1,7):
            if i-k < 0: continue
            dp[i] = (dp[i] + dp[i-k]) % (10**9+7)

    return dp[n] 
n = int(input())
ans = solve(n)
print(ans)