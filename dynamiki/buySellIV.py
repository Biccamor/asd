def solve(k, prices): 
    n = len(prices)

    if k >= n//2:
        ans = 0
        for i in range(1,n):
            if prices[i-1] < prices[i]:
                ans += prices[i]-prices[i-1]
        return ans


    dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)]


    for j in range(1, k+1):
            dp[0][j][0] = -prices[0]

    for i in range(n): 
        for j in range(1, k+1):
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]) # kupuje
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])

    return dp[n-1][k][0]