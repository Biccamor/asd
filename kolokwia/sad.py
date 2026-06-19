def orchard(T,m):
    dp = [(-float('inf'), 0)]*m
    dp[0]=(0,0)

    for num in T:
        new_dp = dp[:]
        for i in range(m-1,-1,-1):
            if dp[i][0]==-float('inf'): continue
            suma = dp[i][0]+num
            r = suma%m 
            if suma > new_dp[r][0]: 
                new_dp[r]=[suma, dp[i][1]+1]
            elif suma == new_dp[r][0]:
                new_dp[r] = [suma, max(new_dp[r][1], dp[i][1]+1)]
        dp = new_dp
    
    suma = dp[0]

    return len(T)-dp[0][1]

T=[2,2,7,5,1,14,7]
m = 7 
print(orchard(T,m))