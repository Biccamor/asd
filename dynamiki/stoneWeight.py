def lastStoneWeightII(stones):

    suma = sum(stones)//2

    dp = [float('inf')]*(suma+1)
    dp[0]=0
    n = len(stones)
    for k in range(0,n):
        for i in range(suma, -1, -1):
            if dp[i] == float('inf'): continue 
        
            if stones[k] + i > suma:
                continue 
            dp[i+stones[k]] = 1


    for i in range(suma,-1,-1):
        if dp[i]!=float('inf'):
            return sum(stones)-i-i
        
stones = [2,7,4,1,8,1]
print(lastStoneWeightII(stones))