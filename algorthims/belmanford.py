def solve(E,n,start):
    dist = [float('inf')]*n 
    dist[start] = 0

    for _ in range(n-1):
        for u,v,waga in E:
            dist[v] = min(dist[v], dist[u]+waga)

    for _ in range(n-1):
        for u,v,waga in E:
            if dist[v] > dist[u] +waga:
                return -1
    return dist 

def solve2(G,n,start):
    dist = [float('inf')]*n 
    dist[start] = 0 

    for _ in range(n-1):
        for u in range(n):
            for v,w in G[u]:
                dist[v] = min(dist[v], dist[u] + w)

    for _ in range(n-1):
        for u in range(n):
            for v,w in G[u]:
                if dist[v] > dist[u] + w:
                    return -1