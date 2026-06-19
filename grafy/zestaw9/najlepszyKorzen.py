def find(G,n, start):
    
    max_dist = -1
    far_node = -1
    vis = [False]*n
    def dfs(u,akt):
        nonlocal max_dist, far_node
        vis[u] = True 
        if akt>max_dist:
            max_dist = akt 
            far_node = u 

        for v,w in G[u]:
            if vis[v]==False:
                dfs(v,akt+w)
    dfs(start, 0)

    return max_dist, far_node

def solve(G,n):

    _, A = find(G,n, 0)

    parent = [None]*n
    max_dist = -1
    far_node = -1
    vis = [False]*n
    dist_A = [float('inf')]*n
    def dfs(u, akt):
        nonlocal max_dist, far_node
        vis[u] = True 
        dist_A[u] = akt
        if akt>max_dist:
            max_dist = akt
            far_node = u 

        for v,w in G[u]:
            if vis[v] == False:
                parent[v] = u
                dfs(v,akt+w)

    dfs(A,0)

    cur = far_node
    srodek = -1 
    aktMin = float('inf')

    while cur != None:
        fromA = dist_A[cur]
        fromB = max_dist - fromA 

        maxi = max(fromA, fromB)

        if maxi < aktMin:
            aktMin = maxi 
            srodek = cur
        cur = parent[cur]

    return srodek