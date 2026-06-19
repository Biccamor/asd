def findMaxForm(strs, m: int, n: int) -> int:
   
    dp  = [[-float('inf')]*(n+1) for _ in range(m+1)]

    dp[0][0] = 0

    T = [(0,0)]*len(strs)

    for i in range(len(strs)):
        zeros = 0
        ones = 0 
        s = strs[i]
        for x in s: 
            if x == "0":
                zeros+=1
            else:
                ones +=1 
        T[i] = (zeros,ones)
    maxi = 0 
    for k in range(0,len(T)):
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i-T[k][0]<0 or j-T[k][1]<0: continue
                dp[i][j] = max(dp[i][j], dp[i-T[k][0]][j-T[k][1]]+1) 
                maxi = max(dp[i][j], maxi)
    return maxi


print(findMaxForm(["10","0001","111001","1","0"], m = 5, n = 3))