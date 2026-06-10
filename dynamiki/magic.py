def magic(C):
    n = len(C)  
    dp = [0]*n 

    for i in range(0, n-1):
        m = C[i][0]
        for d in range(1,4):
            cost, to = C[i][d]
            if to == -1: continue
            if cost <= m:   
                new_money = min(10,m-cost)
                dp[to] = max(dp[to], dp[i]+new_money)
            else:
                akt = dp[i]
                if akt + m >= cost:     
                    new_money = akt - (cost-m)
                    dp[to] = max(dp[to], new_money)
    print(dp)

C2 = [
    [15, [5, 1], [3, 2], [0, -1]],  # Komnata 0 (drzwi do 2 są NIELEGALNE, bo 15-3 = 12 > 10)
    [5,  [0, 2], [0, -1], [0, -1]],  # Komnata 1
    [0,  [0, -1], [0, -1], [0, -1]]   # Komnata 2 (meta)
]

magic(C2)