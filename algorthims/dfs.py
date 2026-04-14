def solve(G):

    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]

    def DFSvisit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                DFSvisit(G,v)
    
    for u in range(n):
        if not visited[u]:
            DFSvisit(G,u)
    print(visited)

G = [
    [1,2],
    [0, 3,4],
    [0,3,5],
    [1,2,5,6],
    [1,6],
    [4,6],
    [3,4,5],
    [8],
    [7,9],
    [8]
]

for i,nodes in enumerate(G):
    print(f"{i}: {nodes}")

solve(G)