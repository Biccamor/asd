import sys
from collections import deque

def read_data():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    n = int(next(iterator))
    m = int(next(iterator)) 
    q = int(next(iterator)) 
    d = int(next(iterator)) 
    
    G = [[] for _ in range(n)]
    E = []
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        c = int(next(iterator))
        
        G[u].append((v, c))
        G[v].append((u, c)) 
        E.append(c)

    queries = []
    for _ in range(q):
        start = int(next(iterator)) - 1
        end = int(next(iterator)) - 1
        queries.append((start, end))
        
    return n, m, q, d, G, queries, E


def solve(G, n, m, d, queries, E):

    def bfs(a,b, min_v, max_v):
        nonlocal n,d 

        vis = [False]*n 
        q = deque()
        q.append(a)
        #minmax = [min, max]
        vis[a] = True
        while q: 
            node = q.popleft()

            if node == b:
                return True

            for v,w in G[node]:
                if vis[v] == True: continue
                if w >= min_v and w <= max_v:
                    q.append(v)
                    vis[v] = True
                
                else:
                    continue

        return False        
    E.sort()

    for a,b in queries:
        f = False
        prev = None
        for e in E: 
            if prev == e: continue
            prev = e
            min = e 
            max = e+d
            if bfs(a,b, min, max)==True:
                print("TAK")
                f = True
                break
        if f == False: 
            print("NIE")



if __name__ == '__main__':

    n, m, q, d, G, queries, E = read_data()
    solve(G,n,m,d,queries, E)