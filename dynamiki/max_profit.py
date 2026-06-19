def jobScheduling(startTime, endTime, profit):
    m = max(endTime)
    dp = [0]*(m+1)

    T = []
    n = len(startTime)
    for i in range(n):
        T.append((startTime[i], endTime[i], profit[i]))
    
    T.sort(key=lambda x: x[1])

    dp[T[0][1]] = T[0][2]
    prev_end = T[0][1]

    for i in range(1,n):
        dp[T[i][1]] = max(dp[T[i][1]], dp[T[i][0]]+T[i][2])
        for j in range(T[i][1],-1,-1):
            if j < T[i][0]:
                dp[T[i][1]] = max(dp[T[i][1]], dp[j]+T[i][2])
            dp[T[i][1]] = max(dp[j], dp[T[i][1]])
    return max(dp)


startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]
jobScheduling(startTime, endTime, profit)