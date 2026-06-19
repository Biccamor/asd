import heapq as hq 

def armstrong(B,E,s,t):
    n = 0
    for i in E: 
        n = max(n, i[0], i[1])
    n+=1 
    G = [[] for _ in range(n)]

    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))


    def dijkstra_rev(start, end=False):
        nonlocal n 
        q = []
        hq.heappush(q, (0,start))
        dist = [float('inf')]*n
        dist[start] = 0
        while q:
            d, node = hq.heappop(q)
            if end == True:
                if node == t: 
                    return d

            if d > dist[node]: continue

            for v, w in G[node]: 
                if d + w < dist[v]: 
                    dist[v] = d+w
                    hq.heappush(q, [d+w, v])

        return dist 
    
    dist_r = dijkstra_rev(t)
    dist = dijkstra_rev(s)
    cost = [float('inf')]*(n+1)
    cost[n] = dijkstra_rev(s,end=True)
    eps = 1e-9
    for i, p, q in B:
        cost[i] = min(dist[i] + p*dist_r[i]/q, cost[i])
        cost[i] = int(cost[i] + eps)
        
    print(cost)
    return min(cost)

if __name__ == "__main__":
    B = [ (1, 1, 2), (2, 2, 3) ]
    G = [ (0,1,6), (1,4,7), (4,3,4),
        (3,2,4), (2,0,3), (0,3,6) ]
    s = 0
    t = 4
    armstrong(B,G,s,t)