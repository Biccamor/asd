from queue import PriorityQueue

def turysta(E,D,L):
    k = 3
    n = 0 
    for u,v,_ in E: 
        n = max(n, u, v)
    n+=1
    G =[[] for _ in range(n)]
    for u,v,w in E:    
        G[u].append((v,w))
        G[v].append((u,w))

    def dijkstra(): 
        nonlocal D, L 

        min_dist = [[float('inf') for _ in range(k+1)] for _ in range(n)]    
        min_dist[D][0]=0
        q = PriorityQueue()
        q.put((0,D,0))

        while not q.empty():
            dist, node, dif = q.get()

            if min_dist[node][dif] < dist: continue 

            if node == L and dif == k: 
                return dist 
            elif node == L and dif < k: continue
            
            for v,w in G[node]:
                if v==L:
                    if dif == k: 
                        q.put((w+dist, v, dif))
                    continue
                if v ==D: continue    
                
                akt_dif = dif+1
                if akt_dif > k: continue

                if w+dist < min_dist[v][akt_dif]:
                    min_dist[v][akt_dif] = w+dist 
                    q.put((w+dist, v, akt_dif))
    
    dist = dijkstra()
    print(dist)

if __name__ == "__main__":
    G = [
    (0, 1, 9), (0, 2, 1),
    (1, 2, 2), (1, 3, 8),
    (1, 4, 3), (2, 4, 7),
    (2, 5, 1), (3, 4, 7),
    (4, 5, 6), (3, 6, 8),
    (4, 6, 1), (5, 6, 1)
    ]
    D = 0
    L = 6
    turysta(G,D,L)
