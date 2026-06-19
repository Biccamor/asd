def kingqueen(V,E,D,K,Q,B):

    G = [[] for _ in range(V)]

    for u,v in E:
        G[u].append(v)
        G[v].append(u)

    vis = [False]*V
    def dfs(u): 
        nonlocal vis 
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                dfs(v)
    ans = 0
    for i in range(D):
        vis = [False]*V
        vis[B[i]] = True 
        dfs(K[i])
        if vis[Q[i]]:
            ans+=1

    return ans 

if __name__ == "__main__":
    V = 9

    E = [(0,1),(0,2),(2,1), (2,3),(5,2),(4,2),
    (3,4),(4,5),(5,6), (8,6),(7,8),(6,7) ]
    D = 3
    K = [0,5,7]
    Q = [3,6,0]
    B = [2,2,5]
    ans = kingqueen(V,E,D,K,Q,B)
    print(ans)