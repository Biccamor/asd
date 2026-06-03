def wired(T):
    n = len(T)
    dp = [[float('inf')]*(n+1) for _ in range(n+1)]

    for i in range(0,n+1):
        for j in range(0,n+1):
            if i>j:
                dp[i][j] = 0

    def dif(a,b):
        return 1+abs(b-a)

    for L in range(2,n+1):
        for i in range(0, n-L+1):
            j = i+L-1
            for k in range(i+1,j+1):
                dp[i][j] = min(dif(T[i], T[k])+dp[k+1][j]+dp[i+1][k-1], dp[i][j])

    return dp[0][n-1]

T = [7,1,3,7,2,1]
wired(T)