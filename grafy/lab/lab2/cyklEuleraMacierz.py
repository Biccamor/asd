"""
Proszę zaimplementować algorytm znajdujący cykl Eulera (rep. macierzowa, graf spójny,
stopnie parzyste).
"""

def solve(G, n): 
    
    order = []
    last = [0]*n

    def dfs(u):

        while last[u] < n:
            v = last[u]
            last[u]+=1  
            
            if G[v][u] == 1:
                G[v][u] = 0 
                G[u][v] = 0                 
                dfs(v)
        
        order.append(u)
    dfs(0)

    order[::-1]
            
    return order 

if __name__ == "__main__":
    G = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0]
    ]

    check = solve(G,len(G))
    print(check)