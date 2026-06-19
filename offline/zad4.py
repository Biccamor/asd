from queue import PriorityQueue
import sys 
import math 

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    g = [[] for _ in range(n + 1)]
    idx = 3 
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        
        g[u].append((v, w))
        g[v].append((u, w))

    queries = []
    for _ in range(k):
        queries.append(int(input_data[idx]))
        idx+=1

    def dijkstra(start):
        nonlocal g, n

        queue = PriorityQueue()
        dist = [float('inf')]*(n+1) 
        dist[start] = 1
        queue.put([math.log(dist[start]),start ])
        parent = [None]*(n+1)
        vis = [False]*(n+1)

        while not queue.empty():

            cur_dist, cur_node = queue.get()
            
            if vis[cur_node]==True:
                continue
            
            vis[cur_node] = True
            
            for v,w in g[cur_node]:
            
                if vis[v] == False:
                    if cur_dist +  math.log(w) < math.log(dist[v]):
                        dist[v] = cur_dist*w
                        parent[v] = cur_node
                        queue.put([math.log(dist[v]), v])

        return parent, dist

    
    parent, dist = dijkstra(1)
    
    for q in queries:

        akt = q
        ans = [] 
        
        while akt is not None:
            ans.append(akt) 
            akt = parent[akt]
        #ans.append(0)
        ans = ans[::-1]
        
        print(len(ans), end=" ")
        for i in ans: print(i, end=" ")
        print(dist[q], end="\n")


solve()