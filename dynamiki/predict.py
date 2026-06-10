def predictTheWinner(nums):
        n=len(nums)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
             dp[i][i] = nums[i]

        for L in range(2,n+1):
            tura = 0 
            for i in range(0, n-L+1):
                j = i+L-1

                dp[i][j] =  
        return dp       

nums = [1,5,2]
print(predictTheWinner(nums))