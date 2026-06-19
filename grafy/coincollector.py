def solve(K,G,n):
    
    order = []
    vis = [False]*n 

    def dfs(u):
        nonlocal G
        vis[u] = True 

        for v in G[u]: 
            if vis[v] == False: 
                dfs(v)

        order.append(u)
    
    for v in range(n):
        if vis[v] == False:
            dfs(v)
    
    G_reverse = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G_reverse[v].append(u)
    
    vis = [False]*n
    

    def dfs_reverse(u, akt):
        nonlocal G_reverse
        akt.append(u)
        vis[u] = True 
        for v in G_reverse[u]: 
            if vis[v] == False: 
                dfs_reverse(v, akt)

    conected = []
    order = order[::-1]
    akt = []
    for u in order: 
        if vis[u]==False:
            akt = []
            dfs_reverse(u, akt)
            conected.append(akt)

    c = len(conected)
    cost = [0]*c
    for i in range(c):
        u = conected[i]
        for v in u:
            cost[i] += K[v]
        
    scc_ids = [-1]*n 

    for i, u in enumerate(conected):
        for v in u:
            scc_ids[v] = i


    dag = [[] for _ in range(c)]
    vis = [False]*c

    for id in range(c): 

        for u in conected[id]:
            for v in G[u]:

                if id != scc_ids[v] and 


if __name__ == "__main__":
    n,m = map(int, input().split())

    K =[]
    for _ in range(n):
        a = int(input())
        K.append(a)

    G = [[] for _ in range(n)]

    for _ in  range(m):
        a, b = map(int, input().split())
        G[a-1].append(b-1)

    solve(K,G,n)