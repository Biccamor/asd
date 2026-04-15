"""sprawdz czy graf w rep macierzowej ma cykl"""

def solve(G,n):
    
    vis = [False]*n
    parent = [None]*n # trzymay rodzicow 
    def dfs(u):
        vis[u] = True 
        for v in range(n): 
            if vis[v] == False and G[u][v]==1: 
                parent[v] = u
                dfs(v)
            elif G[u][v]==1 and vis[v]==True and parent[v] != u: 
                return True 
    
    for i in range(n):
        if vis[i] == False:
            if dfs(i)==True:
                return True
    
    return False 


if __name__=="__main__":
    G = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]

    print(solve(G, len(G)))
