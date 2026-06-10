def f(A,B,C,d):
    return A*d*d + B*d + C

def solve(n,P,A,B,C, T):
    dp = [[-1]*(n+1) for _ in range(n+1)] # indeks liscia x liczba skokow

    dp[0][0] = T[0][1] 


    for i in range(0,n):
        for j in range(0,n):
            if dp[i][j] == -1: continue

            akt_lisc = T[i][0]
            akt_energia = dp[i][j]

            for k in range(i+1, n+1):
                nowy_lisc = T[k][0]
                d = nowy_lisc - akt_lisc
                cost = f(A,B,C,d)
                if akt_energia - cost < 0: 
                    break

                dp[k][j+1] = max(dp[k][j+1], akt_energia-cost+T[k][1])
                
    target_idx = -1
    for idx, lisc in enumerate(T):
            if lisc[0] == P:
                target_idx = idx
                break

    for i in range(n+1):
        if dp[target_idx][i] != -1:
            return i

    return -1

P,n,A,B,C = map(int, input().split())
T = []

for i in range(n):
    x, e = map(int,input().split())
    T.append((x,e))
T.append((P,0))

T.sort(key=lambda x: x[0])
    

print(solve(n,P,A,B,C,T))