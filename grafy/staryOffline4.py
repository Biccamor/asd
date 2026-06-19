from collections import deque 

def solve(E,src,dst,t):
    
    n = 0
    for i in E:
        n = max(i[0], i[1], n)    
    n+=1
    G = [[] for _ in range(n)]

    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    

    def bfs(mini, maxi):
        nonlocal src, dst,n
        
        vis = [False]*n
        q = deque()
        q.append(src)
        vis[src] = True
        while q:
            node = q.popleft()

            if node == dst: 
                return True 

            for v, w in G[node]:
                if vis[v] == True: continue
                if w < mini or w > maxi: 
                    continue 
                q.append(v)
                vis[v] = True

        return False 

    minis = [v[2] for v in E]
    
    for p in minis:
        maxi = p+2*t 
        check = bfs(p, maxi)
        if check == True:
            print(p, maxi, p+t)
            return True 
    
    return False



if __name__ == "__main__":
    L = [(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),
    (2,5,2300),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)]
    x = 0
    y = 6
    t = 60

    solve(L,x,y,t)
