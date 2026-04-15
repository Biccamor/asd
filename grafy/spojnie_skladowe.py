def solve(G): # G w postaci listowej
    n = len(G) 
    vis = [False] * n 

    def dfs(G, u):
        vis[u] = True

        for v in G[u]:
            if vis[v] == False:
                dfs(G,v)
            
    count = 0
    for u in range(n):
        if vis[u] == 0:
            count +=1  
            dfs(G,u)   
    
    return count