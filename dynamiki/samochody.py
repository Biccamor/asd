def dp(L,A):
    suma = 0
    koniec = len(A) 
    for i in range(len(A)):
        if suma + A[i] <= 2*L:
            suma += A[i]
        else: 
            koniec = i 
            break 

    x = 2*L - suma 
    dp = [0]*(L+1)
    dp[0] = 1 

    for i in range(koniec):
        for j in range(L-1, -1, -1):
            if dp[j] == 1:
                if j + A[i] <= L:
                    dp[j+A[i]] = 1 

    for i in range(L-x, L+1):
        if dp[i] == 1:
            return koniec

    for i in range()        
    