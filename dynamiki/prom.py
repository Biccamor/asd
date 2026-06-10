def solve(A, L):
    n = len(A)
    x = 2*L-sum(A)

    dp = [False]*(2*L+1) 
    dp[0]=True
    akt = 0
    for i in range(n, -1, -1):

        if dp[i] == False: continue

        if i + akt < L: 
            dp[i+akt] = True
        
        