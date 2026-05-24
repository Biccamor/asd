def maxSumDivThree(nums) -> int:
    dp = [0,-float('inf'),-float('inf')]
    
    for i in range(len(nums)):
        next_dp = dp[:]
        for j in range(3):
            if dp[j]==-float('inf'): continue
            suma = dp[j] + nums[i]
            next_dp[suma%3] = max(dp[suma%3], dp[j]+nums[i])
        dp = next_dp
    return dp[0]

nums = [4]
print(maxSumDivThree(nums=nums))