from queue import PriorityQueue

def dijkstra(G,src):
    n = len(G)
    parent = [None]*n 
    dist = [float('inf')]*n
    queue = PriorityQueue()
    queue.put([0, src])
    dist[src] = 0
    while not queue.empty(): 
        d, u = queue.get()  

        if d > dist[u]: continue

        for v in range(n): 
            
            if G[u][v] != -1 and dist[v] > d + G[u][v]: 
                dist[v] = d +G[u][v] 
                parent[v] = u
                queue.put([G[u][v], v])
    return dist 

if __name__ == "__main__":

    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0]
                ]
    
    G = [[-1, 7, 5, 2, -1, -1],
     [7, -1, -1, -1, 3, 8 ],
     [5, -1, -1, 10, 4, -1],
     [2, -1, 10, -1, -1, 2], 
     [-1, 3, 4, -1, -1, 6],
     [-1, 8, -1, 2, 6, -1]]

    distance = dijkstra(G, 0)