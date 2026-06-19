def solve(G,price,x,y,r):
    n = len(G)

    min_dist = [[float('inf'), float('inf')] for _ in range(n)]
    V = 2*n -1 

    for _ in range(V):
        ruch = False

        for u in range(n):

            if min_dist[u][0] != float('inf'):
                koszt = min_dist[u][0] - price[u]
                if koszt < min_dist[u][1]:
                    min_dist[u][1] = koszt 
                    ruch = True 

            for v, w in G[u]:
                if min_dist[u][0] != float('inf'): 
                    if min_dist[v][0] > min_dist[u][0] + w:
                        min_dist[v][0] = min_dist[u][0] + w 
                        ruch = True 
                if min_dist[u][1] != float('inf'): 
                    if min_dist[v][1] > min_dist[u][1] + w*2 +r :
                        min_dist[v][1] = min_dist[u][1] + w*2 + r 
                        ruch = True
        if ruch == False: break