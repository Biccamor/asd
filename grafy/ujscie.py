def ujscie(G, n):
    kandydat = 0
    for k in range(n): 
        if G[kandydat][k] == 1: 
            kandydat = k
    
    for i in range(n):
        if i == kandydat: continue 
        if G[i][kandydat]==0:
            return -1
    return kandydat