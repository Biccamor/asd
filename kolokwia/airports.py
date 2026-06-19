import heapq as hq

def solve(G, A, s, t):

    G.append([])
    n = len(G)

    for i, a in enumerate(A): 
        G[n-1].append([i,a])
        G[i].append([n-1,a])


    def dijkstra():
        nonlocal s, t, n
        q = []
        dist = [float('inf')]*n 

        hq.heappush(q, [0, s])
        while q: 
            w, node = hq.heappop(q)

            if t == node: return w 

            if w > dist[node]: continue

            for v, w_n in G[node]: 
                if w_n + w >= dist[v]: continue
                
                dist[v] = w + w_n
                hq.heappush(q, [w+w_n,v])
        return -1 
    
    cost = dijkstra()
    print(cost)

if __name__ == "__main__":
    G = [[(1,3), (3,2)],
         [(0,3), (2,20)],
         [(1,20), (5,1), (3,6)],
         [(0,2), (2,6), (4,1)],
         [(3,1), (5,7)],
         [(4,7), (2,1)]
         ]
    A =[50,100,1,20,2,70]
    s=0
    t=5
    solve(G,A,s,t)
    