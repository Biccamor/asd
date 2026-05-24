def solve(N):
    dp = [0]*N 

    dp[0] = 1 
    dp[1] = 2
    dp[2] = 7 

    for i in range(3, N):
        dp[i]= (3*dp[i-1] + dp[i-2] - dp[i-3]) % 67

    return dp 

q = int(input())
queries = [int(input()) for _ in range(q)]
dp = solve(max(queries)+1)

for i in range(q):
    print(dp[queries[i]-1])
