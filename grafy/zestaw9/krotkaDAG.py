def solve(G, s):
    n = len(G)
    order = []
    vis = [False]*n 

    def dfs(u):
        vis[u] = True 
        for v,w in G[u]:
            if vis[v]==False:
                dfs(v)
        order.append(u)
    
    dfs(s)
    order = order[::-1]

    dist = [float('inf')]*n 
    dist[s] = 0
    for u in order:
        if dist[u] == float('inf'): continue
        for v, w in G[u]:
            if dist[v] >  dist[u] + w:
                dist[v] = dist[u]+w 
    return dist
    