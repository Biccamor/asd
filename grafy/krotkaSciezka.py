from collections import deque

def solve(G,start,target):
    n = len(G)
    parent = [None]*n
    vis = [False]*n 

    def bfs(g,u, target):
        queue = deque([u])
        vis[u] = True

        while queue:
            cur = queue.popleft()
            if cur == target:
                break
            for v in g[cur]: 
                if vis[v] == False:
                    parent[v] = cur
                    queue.append(v)
                    vis[v] = True

        return parent

    parent = bfs(G,start,target)
    if parent[target]==None and start!=target : 
        return []

    path = [target]
    akt = target 
    while akt != start:
        akt = parent[akt]
        path.append(akt)

    return path[::-1]

if __name__ == "__main__":
    graph_1 = [    
        [1, 4],
        [0, 2],
        [1, 3],
        [2, 4],
        [0, 3]
    ]
    start = 0
    target = 3 
    ans = solve(graph_1, start, target)
    print(ans)