def solve(D,C,T,E): # E to jest paliwo T to teleporty od i do j za p  D to odleglosci miedzy planetami C to ceny
    
    n = len(D)
    dp = [[float('inf')]*(E+1) for _ in range(n)]
    dp[0][0] = 0

    for i in range(n-1):
        cena = C[i]
        odl = D[i+1]-D[i]
        skok, cena_t = T[i]

        for e in range(E, -1, -1):
            if dp[i][e] == float('inf'):
                continue
        
            dp[skok][0] = min(dp[skok][0], dp[i][e]+cena_t)

            for k in range(0, E-e+1):
                akt_e = e+k
                if akt_e >= odl:
                    dp[i+1][akt_e-odl] = min(dp[i][e]+cena*k, dp[i+1][akt_e-odl])
    print(dp)
    return min(dp[n-1])


D = [ 0, 5, 10, 20]
C = [ 2, 1, 3, 9]
T = [(2,3), (3,7), (2,10), (3,10)]
E = 10

print(solve(D,C,T,E))
