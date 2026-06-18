def solve(V,E,D,K,Q,B):
    G = [[] for _ in range(V)]

    for u,v in E:
        G[u].append(v)
        G[v].append(u)


    def dfs(u,b,vis):    
        if u == b: return vis

        for v in G[u]:
            if vis[v]: continue
            vis[v] = True
            dfs(v, b, vis)

        return vis
    ans = 0

    for i in range(D):

        vis = [False]*V
        vis[B[i]] = True
        akt = dfs(K[i], Q[i], vis)
        if vis[Q[i]]:
            ans+=1
    
    return ans 


V = 9
E = [(0,1),(0,2),(2,1), (2,3),(5,2),(4,2),
(3,4),(4,5),(5,6), (8,6),(7,8),(6,7) ]
D = 3
K = [0,5,7]
Q = [3,6,0]
B = [2,2,5]

print(solve(V,E,D,K,Q,B))