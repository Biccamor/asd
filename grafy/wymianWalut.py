def wymiana(K):
    n = len(K)

    cost = [[K[i][j] for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cost[i][k] != float('inf') and cost[k][j] != float('inf'):
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
                
    
    for i in range(n):
        if cost[i][i] < 0:
            return -1 
    maxi = 0
    for i in range(n):
        for j in range(n):
            if cost[i][j] > maxi and cost[i][j] != float('inf'): 
                maxi = cost[i][j]
                
    return maxi