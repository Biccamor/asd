def maze(L):
    n = len(L)
    dp =[[0]*n for _ in range(n)]
    dp[0][0] = 0
    