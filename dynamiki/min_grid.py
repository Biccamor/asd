def minPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[float('inf')]*m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
    
    return dp[n-1][m-1]


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    ans = minPathSum(grid)
    print(ans)