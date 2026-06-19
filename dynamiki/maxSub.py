def maximumSum(arr):
    n = len(arr)
    dp = [[-float('inf')]*2 for _ in range(n+1)]
    dp[0][0]=arr[0]
    dp[0][1]=-float('inf')
    maxi = -float('inf')
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
        dp[i][1] = max(dp[i-1][1]+arr[i], dp[i-1][0])
    maxi = -float('inf')
    print(dp)
    for i in range(0,n):
        maxi = max(dp[i][0], dp[i][1], maxi)
    return maxi

arr = [-1,-1,-1,-1]
print(maximumSum(arr))