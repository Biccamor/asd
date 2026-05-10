def solve(n):
    dp = [float('inf')]*(n+1)
    dp[1] = 1
    dp[0] = 0 
    for i in range(2,n+1):
        num = str(i)
        for c in num:
            dp[i] = min(dp[i], dp[i-int(c)]+1)
    return dp[n]

n = int(input())
print(solve(n))