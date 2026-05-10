def solve(v,w,h, W, H):
    dp = [[0]*(H+1) for _ in range(W+1)]
    n = len(v)

    for i in range(n):
        waga = w[i]
        wys = h[i]
        wart = v[i]

        for j in range(W, waga-1, -1):
            for k in range(H, wys-1, -1):
                dp[j][k] = max(dp[j][k], dp[j-waga][k-wys]+wart)
    return dp[W][H]