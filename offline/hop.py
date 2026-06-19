p = 10**9 + 696969

def pre_proces(n, m, A, B, k=200):
    dp_x = [[0]*(k+1) for _ in range(n+1)]
    dp_y = [[0]*(k+1) for _ in range(m+1)]
    dp_x[1][0] = 1
    dp_y[1][0] = 1

    for i in range(1, n+1):
        for e in range(0, k+1):
            for a in range(0, A+1):  
                if i + a > n or e+1 > k: continue
                dp_x[i+a][e+1] = (dp_x[i+a][e+1] + dp_x[i][e]) % p

    for j in range(1, m+1):
        for e in range(0, k+1):
            for b in range(0, B+1): 
                if j + b > m or e+1 > k: continue
                dp_y[j+b][e+1] = (dp_y[j+b][e+1] + dp_y[j][e]) % p

    return dp_x, dp_y

def solve(dp_x, dp_y, k, x, y):
    return (dp_x[x][k] * dp_y[y][k]) % p  

n, m, A, B = map(int, input().split())
q = int(input())


queries = []

max_k = 0
for i in range(q):
    k, x, y = map(int, input().split())
    queries.append((k,x,y))
    max_k = max(max_k, k)

dp_x, dp_y = pre_proces(n, m, A, B, max_k)
import sys
sys.stdout.write('\n'.join(str((dp_x[x][k] * dp_y[y][k]) % p) for k, x, y in queries) + '\n')

