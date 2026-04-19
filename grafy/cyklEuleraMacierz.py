"""
Proszę zaimplementować algorytm znajdujący cykl Eulera (rep. macierzowa, graf spójny,
stopnie parzyste).
"""

def solve(G, n): 
    
    vis = [False]*n
    
    def dfs(u,G): 
        vis[u] = True 

        for v in range(n):

            if G[v][u] == 1:
                G[v][u] = 0 
                G[u][v] = 0                 
                dfs(v,G)
        return False 
    akt = 0
    for i in range(n): 
        if vis[i] == False:
            if akt>=1: return False  
            akt+=1
            if dfs(i,G) == True: 
                return True
            


if __name__ == "__main__":
    G = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0]
    ]


