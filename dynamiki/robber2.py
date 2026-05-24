def solve(nums):
    n = len(nums)
    dp = [0]*n 
    dp[0] = nums[0]
    if len(nums)==1: return dp[0]

    dp[1] = max(nums[0], nums[1])
    for i in range(2, n-1): 
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    dp_end = [0]*n
    dp_end[n-1] = nums[n-1] 
    dp_end[n-2] = max(nums[n-1], nums[n-2])
    
    for i in range(n-3, 0, -1):
        dp_end[i] = max(dp_end[i+1], dp_end[i+2]+nums[i])

    return max(dp_end[1], dp[n-2])



nums = [1,2,3]
print(solve(nums))