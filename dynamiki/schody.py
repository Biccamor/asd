def stairs(k):
    dp = [0]*(k+1)
    dp[1] = 1 

    for i in range(9, k+1):
        dp[i] = dp[i-1] + dp[i-3] +  dp[i-8]