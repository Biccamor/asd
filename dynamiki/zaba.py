def solve(E):
    n = len(E)

    dp = [[float('inf')]*n for _ in range(n)]
    dp[0][0] = 0
    dp[0][E[0]] = 0


    for i in range(n-1, -1, -1):
        for e in range(n-1,-1,-1):
            if dp[i][e] == float('inf'): continue

            for j in range(i+1, n-1):
                if j-i > e: break
                dp[j][e-(j-i)+E[j]] = min(dp[i][e]+1, dp[j][e-(j-i)+E[j]])
