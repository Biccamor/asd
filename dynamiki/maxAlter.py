def solve(T):
    n = len(T)
    dp = [[-float('inf'), -float('inf')] for _ in range(n)]
    dp[0][0] = T[0]

    for i in range(1,n):
        dp[i][1] = max(dp[i-1][0]-T[i], dp[i-1][1])
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+T[i], T[i])

    return dp[n-1][0]

T = [6,2,1,2,4,5]
solve(T)