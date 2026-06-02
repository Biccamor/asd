def kom(X,Z,W):

    n = len(X)
    dp = [[-float('inf')]*(W+1) for _ in range(n)]
    
    dp[0][W] =0
    if Z[0] <= W:
        dp[0][W-Z[0]] = X[0]

    for i in range(0,n-1):
        for j in range(0,W+1):
            if dp[i][j] == -float('inf'): continue
            
            if dp[i][j]-X[i+1] >= 0:
                akt_w = min(W,j+Z[i+1])
                dp[i+1][akt_w] = max(dp[i+1][akt_w], dp[i][j]-X[i+1]) # leczymy sie
            
            if j - Z[i+1] >= 0:
                dp[i+1][j-Z[i+1]] = max(dp[i+1][j-Z[i+1]], dp[i][j]+X[i+1]) # dostajemy punkty
            
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]) # nic nie robimy

    return max(dp[n-1])


X = [3,2,2,3]
Z = [1,3,2,3]
W = 5
print(kom(X,Z,W))