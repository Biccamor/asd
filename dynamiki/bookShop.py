def solve(H,S,m,n):
    dp = [0]*(m+1) 

    for i in range(n):
        for j in range(m, H[i]-1, -1):
            
            dp[j] = max(dp[j], dp[j-H[i]]+S[i])
    return max(dp)

n, x = map(int, input().split())    

# Wczytanie drugiej linii jako listy cen
prices = list(map(int, input().split()))

# Wczytanie trzeciej linii jako listy stron
pages = list(map(int, input().split()))

print(solve(prices,pages,x,n))
