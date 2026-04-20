"""Znajdz sciezke hamiltona (przechodzaca przez kazdy v)"""

def solve(G,n):
    vis = [False]*n
    order = []
    def dfs(u):
        nonlocal order, G, vis 

        vis[u] = True 
        for v in G[u]: 
            if vis[v] == False:
                dfs(v)
        order.append(u)
    
    for i in range(n): 
        if vis[i] == False:
            dfs(i)
    
    order = order[::-1]
    prev = order[0]    
    
    for v in order[1:]:
        if v not in G[prev]: 
            return False 
        prev = v 
    return True 

if __name__ == "__main__": 
    G = [[1,2,4],[2,3],[3],[4], []]
    n = 5
    check = solve(G,n)
    print(check)