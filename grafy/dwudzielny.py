"""
Proszę zaimplementować testowanie, czy graf jest dwudzielny, używając BFS
dla reprezentacji listowej.
"""
from collections import deque


def solve(g):
    n = len(g)
    color = [-1]*n
    
    def bfs(g,v,n): 
        queue = deque([v])
        color[v] = 0
        
        while queue:
            
            cur = queue.popleft()

            for adj in g[cur]:
                if color[adj] != -1:
                    if color[adj] == color[cur]: return False 

                if color[adj] == -1:
                    queue.append(adj)
                    if color[cur]==0:
                        color[adj] = 1
                    else:
                        color[adj] = 0
        return True
    

    for i in range(n):
        if color[i] == -1:
            if bfs(g,i,n) == False:
                return False 
    
    return True 

if __name__ == "__main__":

    G = [
        [4, 5],
        [4, 5],
        [5, 6, 7],
        [6, 7],
        [0, 1],
        [0, 1],
        [2, 3],
        [2, 3],
        [9],
        [10],
        [9]
    ]
    n = 11
    print(solve(G))