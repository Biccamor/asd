import heapq as hp 

def space(n,E,S,a,b):

    G = [[] for _ in range(n+1)]

    for u,v,w in E: 
        G[u].append([v,w])
        G[v].append([u,w])
    
    for s in S: 
        G[s].append([n,0])
        G[n].append([s,0])

    
    def dijkstra():
        nonlocal a, b 
        q = []
        hp.heappush(q, [0, a])
        dist = [float('inf')]*(n+1)
        dist[a] = 0
        vis_space = [False]*(n+1)

        while q:
            cur, node  = hp.heappop(q)
            if node == b: 
                return cur 

            if cur > dist[node]: continue

            for v, w in G[node]:
                #if v == n: 
                #    hp.heappush(q, [cur, v]) 
                if dist[v] <= w + cur: 
                    continue

                dist[v] = w + cur 
                hp.heappush(q, [cur+w, v])

        return -1

    cost = dijkstra()
    print(cost)

if __name__ == "__main__":
    E = [(0,1, 5),
    (1,2,21),
    (1,3, 1),
    (2,4, 7),
    (3,4,13),
    (3,5,16),
    (4,6, 4),
    (5,6, 1)]
    S = [ 0, 2, 3 ]
    a = 1
    b = 5
    n = 7
    space(n,E,S,a,b)