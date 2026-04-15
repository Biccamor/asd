"""
Sprawdzanie czy jest sciezka hamiltona w dagu
"""

def solve(g, n):
    visited = [False]*n
    order = []

    def dfs(g,u,order):
        visited[u] = True
        
        for v in g[u]: 
            if visited[v] == False:
                dfs(g,v,order)

        order.append(u)
    
    for i in range(n):
        if visited[i] == False:
            dfs(g,i,order)
    order = order[::-1]
    prev = order[0]
    for i in order[1:]:
        if i not in g[prev]:
            return False
        prev = i

    return True


if __name__ == "__main__":
    v = [(0, 1), (1, 2), (2, 3), (0, 2), (1, 3)]
    n=4
    G = [[] for _ in range(n)]
    for i in v:
        G[i[0]].append(i[1])
    
    print(solve(G,n))