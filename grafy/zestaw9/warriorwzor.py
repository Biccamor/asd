from collections import deque

def solve(E,s,t):
    n = 0 

    for e in E: 
        n = max(e[0], e[1], n)

    G = [[] for _ in range(n)]
    last = n
    for u,v,w in E:
        if w == 1:
            G[u].append(v)
            G[v].append(u)
        else:
            cur = u 
            for _ in range(w-1):
                G.append([])
                G[cur].append(last)
                G[last].append(cur)
                cur = last 
                last += 1
            G[last-1].append(v)
            G[v].append(last-1)
    

    for u in range(n):
        cur = u
        for _ in range(7):
            G.append([])
            G[last].append(cur)
            G[cur].append(last)
            cur = last
            last+=1
        G[last-1].append(u)
        G[u].append(last-1)

    m = len(G)
    def bfs():
        nonlocal s,t,m 
        vis = [False]*m 
        q = deque()
        q.append((s, 16))

        while q: 
            node, energy = q.popleft()

            for v in G[node]:
                if vis[v]==False:
                    q.append()
