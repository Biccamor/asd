def solve(T, k):
    n = len(T)
    dp = [[0]*(n) for _ in range(k+1)]
    ans = T[0]
    for i in range(0,k+1):
        dp[i][0] = T[0]
        for j in range(1,n):
            cur = max(dp[i][j-1]+T[j], T[j])
            if i==0:
                dp[i][j] = cur 
                continue
            dp[i][j] = max(dp[i][j-1]+T[j], dp[i-1][j-1], T[j])
            if dp[i][j] > ans: ans = dp[i][j]
    return ans


T = [-20, 5, -1, 10, 2, -8, 10]
print(solve(T,1))