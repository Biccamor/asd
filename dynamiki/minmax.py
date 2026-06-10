def solve(A, k):
    n = len(A)
    sumy = [0]*n 
    sumy[0] = A[0]

    for i in range(1,n):
        sumy[i] = sumy[i-1]+A[i]

    dp = [[0]*(k+1) for _ in range(n)]

    dp[0][1] = sumy[0]
    for i in range(1,n):
        dp[i][1] = sumy[i]

    
    for p in range(2, k+1): 
        for i in range(p-1, n):
            for j in range(p-2, i):

                dp[i][p]=max(dp[i][p], min(dp[j][p-1], sumy[i]-sumy[j]))

    return dp[n-1][k]
