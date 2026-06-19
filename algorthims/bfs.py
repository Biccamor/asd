from collections import deque

def bfs(G, n,u):

    vis = [False]*n
    parent = [None]*n
    q = deque([u])
    vis[u] = True 

    while q: 
        u = q.popleft()

        for v in G[u]: 
            if vis[v] == False:
                parent[u]=v
                q.append(v)
                vis[v]=True
    