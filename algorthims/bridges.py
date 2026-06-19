def findBridge(connections,n):
    g =  [[] for _ in range(n)]

    for c in connections:
        g[c[0]].append(c[1])
        g[c[1]].append(c[0])

    tin = [-1]*n
    low = [-1]*n 
    bridges = []
    time = 1 
    
    def dfs(u, parent):
        nonlocal tin, low, g, time 

        tin[u] = time
        low[u] = time 
        time+=1 

        for v in g[u]:
            if v == parent: continue 

            if tin[v] == -1: 
                
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if low[v] > tin[u]:
                    bridges.append([u,v])    

            else:
                low[u] =  min(low[u], tin[v])
    
    for i in range(n):
        if tin[i]==-1:
            dfs(i,-1)
    
    return bridges

if __name__ == "__main__":
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    g =  [[] for _ in range(n)]

    for c in connections:
        g[c[0]].append(c[1])
        g[c[1]].append(c[0])

    bridge = findBridge(g,n)

    print(bridge)