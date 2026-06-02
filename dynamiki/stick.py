def solve(n, cuts):
    
    cuts.sort()
    cuts = [0] + cuts + [n]
    N = len(cuts)-1
    dp = [[0]*N for _ in range(N)]

    for L in range(2, N+1):
        for i in range(0,N-L+1):
            j = i+L-1
            dp[i][j] = float('inf')

            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cuts[j+1] -  cuts[i] ) 
    
    return dp[0][N-1]
n = 7
cuts = [1,3,4,5]
print(solve(n,cuts))