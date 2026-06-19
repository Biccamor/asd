from queue import PriorityQueue

def dijkstra(g, n, start):

    queue = PriorityQueue()
    dist = [float('inf')]*n 
    dist[start] = 0
    queue.put([dist[start],start ])
    parent = [None]*n
    vis = [False]*n

    while not queue.empty():

        cur_dist, cur_node = queue.get()
        
        if vis[cur_node]==True:
            continue
        
        vis[cur_node] = True
        
        for v,w in g[cur_node]:
        
            if vis[v] == False:
                if cur_dist + w < dist[v]:
                    dist[v] = cur_dist+w
                    parent[v] = cur_node
                    queue.put([dist[v], v])

    return dist, parent


if __name__ == "__main__":
    n = 5
    g = [
    [(1, 4), (2, 2)],
    [(3, 10), (2, 5)],
    [(1, 1), (4, 3)],
    [(4, 11)],
    [(3, 4)]
    ]
    start =0 
    dist, parent = dijkstra(g,n,0)
    print(dist)
    print(parent)