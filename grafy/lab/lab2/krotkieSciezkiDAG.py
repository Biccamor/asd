def solve(G,n,s):
    vis = [False]*n 
    order = []
    def dfs(u):
        vis[u] = True
        for v in G[u]:
            if not vis[v[0]]:
                dfs(v[0])
        order.append(u)

    for i in range(n):
        if not vis[i]:
            dfs(i)
    
    order = order[::-1]

    
    idx = 0
    for i in range(len(order)):
        if order[i] == s:
            idx = i 
            break
    
    dist = [float('inf')]*n 
    dist[s] = 0 

    for u in order[idx:]: 
        if dist[u] == float('inf'): continue

        for v in G[u]:
            if dist[u] + v[1] < dist[v[0]]:
                dist[v[0]] = dist[u] + v[1]

    return dist

if __name__ == "__main__":
    edge = [[0, 1, 50], [0, 2, 5], [2, 1, 5]] 
    n = 3 
    G = [[] for _ in range(n)]
    for v in edge:
        if len(v) == 2: w = 1 
        else: w = v[2]
        G[v[0]].append([v[1], w])
    solve(G,n,0)
    #[0, 10, 5]