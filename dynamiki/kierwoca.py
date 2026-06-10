def solve(P,B):
    for i in range(len(P)):
        P[i] = (P[i][0], P[i][1], i)
    P.sort(key=lambda x: x[0])
    
    switch = []

     
    if P[0][1] == 'p':
        switch.append((P[0][0], 0))
    prefiks = P[1][0]-P[0][0]
    for i, (p, t ,idx) in enumerate(P[1:]):
        if t == 'p':
            switch.append((p,prefiks, idx))
        else:
            prefiks += 1
    n=len(switch)
    #switch.append((B, switch[n-1][1]+B-P[len(P)-1][0]))

    #n = len(switch)
    dp = [[float('inf')]*2 for _ in range(n)]
    dp[0][1] = 0 
    dp[1][1]=0
    dp[2][1]=0

    for i in range(1,n):

        if i-3 < 0: 
            if i-2 < 0:
                end = 0 
            else: end = i -2 
        else: end = i-3

        for j in range(i-1,end-1,-1):

            dp[i][1] = min(dp[i][1], dp[j][0]) # Jacek za darmo
            
            dp[i][0] = min(dp[i][0], dp[j][1]+switch[i][1]-switch[j][1]) # Marian

    print(dp)
    print(switch)

# 0 1 2 3 4 5 6 7 8 9
P = [(1,'c'),(3,'c'),(4,'c'),(6,'c'),(8,'c'),(9,'c'),(11,'c'),(13,'c'),(16,'c'),(17,'c'),
(2,'p'),(5,'p'),(7,'p'),(10,'p'),(12,'p'),(14,'p'),(15,'p'),(18,'p')]
# 10 11 12 13 14 15 16 17
B = 20

print(solve(P,B))