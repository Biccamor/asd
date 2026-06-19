from queue import PriorityQueue

def solve(G,E,n,x,y):
    def dijkstra():
        nonlocal n,x,y
        min_dist = [[float('inf') for _ in range(E+2)] for i in range(n)]
        q = PriorityQueue()
        q.put((0,x,E+1))
        min_dist[0][E+1] = 0

        while not q.empty(): 
            dist, node, last = q.get()

            if min_dist[node][last] < dist: continue
            
            if y == node: 
                return dist

            for v,w in G[node]:
                if last < w: continue

                if min_dist[v][w] > dist + w: 
                    min_dist[v][w] = dist + w 
                    q.put((dist+w, v, w))

    dist = dijkstra()
    print(dist)


def solve2(E,n,x,y):
    bucket = [None]*(len(E)+1)
    for e in E: 
        bucket[e[2]]=(e[0],e[1],e[2])
    bucket = bucket[::-1]

    dp = [float('inf')]*n 
    dp[x] = 0 

    for waga in range(len(bucket)): 

        if bucket[waga] is None: continue

        u,v,w = bucket[waga]

        if dp[u] != float('inf'):
            dp[v] = min(w+dp[u], dp[v])
        if dp[v] != float('inf'):
            dp[u] = min(w+dp[v], dp[u])

    return dp[y]


if __name__ == "__main__":
    V = 5
    krawedzie = [
        (0, 1, 6), (0, 2, 5), (2, 3, 4), 
        (3, 4, 3), (1, 4, 2), (1, 3, 1)
    ]
    G = [[] for _ in range(V)]
    for u,v,w in krawedzie:
        G[u].append((v,w))
        G[v].append((u,w))

    ans =solve2(krawedzie, V, 0, 4)
    print(ans)