def solve(G):
    n = len(G)
    znaleziony = [True, -1]
    for a in range(n):
        znaleziony = [True, a]
        for i in range(n): # wiersz
            if G[a][i] == 1:
                znaleziony = [False, -1] 
                break 
        
    
    for j in range(n):
        if j!=znaleziony[1] and G[j][znaleziony[1]] == 0:
            return -1
        
    return znaleziony[1]