def critical(V,E):
    G = [[] for _ in range(V)]
    
    for u,v in E:
        G[u].append(v)

    def dfs(start, u,end,vis):

        if end == u: 
            return vis

        for v in G[u]:
            if u == e1 and v == e2: continue
            if vis[v]: continue
            vis[v] = True
            dfs(start, v,end,vis) 

        return vis
    
    for e1,e2 in E: 
        vis = [0]*V
        vis = dfs(e1, e1,e2,vis)
        if vis[e2]==True:  
            print(f"{e1}, {e2}, TAK")
        else:
            print(f"{e1}, {e2}, NIE")

V = 4
E = [ (0,1), (0,2), (0,3),
(1,2), (1,3), (2,3) ]
critical(V,E)