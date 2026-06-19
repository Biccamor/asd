import heapq as hq 

def solve(G,V,s,t,r):
    n = len(G)

    def dijkstra_reverse():
        nonlocal t,n,r
        min_dist = [float('inf')]*n
        q = []
        min_dist[t] = 0
        hq.heappush(q,(0, t))

        while q: 
            dist,node = hq.heappop(q)

            if dist > min_dist[node]:continue

            for v, w in G[node]:
                if min_dist[v] > dist + 2*w + r: 
                    min_dist[v] = dist + 2*w + r 
                    hq.heappush(q,(dist+2*w+r, v))
        return min_dist

    dist_t = dijkstra_reverse()
    
    def dijkstra():
        nonlocal s,n
        min_dist = [float('inf')]*n
        q = []
        min_dist[s] = 0
        hq.heappush(q,(0, s))

        while q: 
            dist,node = hq.heappop(q)

            if dist > min_dist[node]:continue

            for v, w in G[node]:
                if min_dist[v] > dist + w: 
                    min_dist[v] = dist +w  
                    hq.heappush(q,(dist+w, v))
        return min_dist
    
    dist_s = dijkstra()

    cost = [float('inf')]*(n+1) 

    for i in range(n):
        cost[i] = dist_s[i] + dist_t[i] - V[i]

    def dijkstra_nosteal():
        nonlocal s,t,n
        min_dist = [float('inf')]*n
        q = []
        hq.heappush(q, (0,s))
        min_dist[s] = 0
        while q:
            dist, node = hq.heappop(q)

            if dist > min_dist[node]: continue

            if t == node: return dist 
            
            for v, w in G[node]:
                if min_dist[v] > dist + w: 
                    min_dist[v] = dist +w  
                    hq.heappush(q,(dist+w, v))
        return -1

    cost[n] = dijkstra_nosteal()
    print(cost)
    return min(cost)

if __name__ == "__main__":
    G = [[(1,9), (2,2)], # 0
    [(0,9), (3,2), (4,6)], # 1
    [(0,2), (3,7), (5,1)], # 2
    [(1,2), (2,7), (4,2), (5,3)], # 3
    [(1,6), (3,2), (6,1)], # 4
    [(2,1), (3,3), (6,8)], # 5
    [(4,1), (5,8)] ] # 6
    V = [25,30,20,15,5,10,0]
    s = 0
    t = 6
    r = 7
    solve(G,V,s,t,r)