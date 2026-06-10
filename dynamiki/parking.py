def parking(X,Y):
    n = len(X)
    m = len(Y)
    
    dp = [[float('inf')]*m for _ in range(n)]
    dp[0][0] = abs(X[0]-Y[0])

    for i in range(1,m):
        dp[0][i] = min(dp[0][i-1], abs(X[0]-Y[i]))

    for i in range(1,n):
        for j in range(1,m):

            odl = abs(X[i]-Y[j])   
            
            dp[i][j] = min(dp[i-1][j-1]+odl, dp[i][j-1], dp[i][j])
    
    print(dp)


X =  [3,6,10,14]
Y = [1,4,5,10,11,13,17]
parking(X,Y)    