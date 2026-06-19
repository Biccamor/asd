def solve(G, n):
    order = []
    vis = [False]*n
    
    def dfs(u):
        vis[u] = True 
        for v in G[u]:
            if vis[v]==False:
                dfs(v)
        order.append(u)
    
    vis = [False]*n 
    dfs(order[-1])

    for v in vis:
        if v==False:
            return -1 
    
    return order[-1]



    