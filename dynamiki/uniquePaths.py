def solve(obstacleGrid):
    n = len(obstacleGrid)
    m = len(obstacleGrid[0])
    dp = [[0]*m for _ in range(n)]
    if obstacleGrid[0][0] == 1: return 0 
    for i in range(m):
        if obstacleGrid[0][i] != 1:
            dp[0][i] = 1
    for i in range(n): 
        if obstacleGrid[i][0] != 1:
            dp[i][0] = 1
    
    for i in range(1,n):
        for j in range(1,m):
            if obstacleGrid[i][j] == 1: continue 
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n-1][m-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0]]
    solve(obstacleGrid)