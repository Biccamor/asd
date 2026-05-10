def solve(t, coins):
    dp = [float('inf')] * (t + 1)
    dp[0] = 0

    for c in coins:
        for i in range(c, t + 1):
            nowy_wynik = dp[i - c] + 1
            if nowy_wynik < dp[i]:
                dp[i] = nowy_wynik
                
    return dp[t]

def main():
    n, w = map(int, input().split())
    
    tablica = list(map(int, input().split()))

    ans = solve(w,tablica)
    if ans == float('inf'): print(-1)
    else: print(ans)

if __name__ == "__main__":
    main()