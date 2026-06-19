from queue import PriorityQueue

def solve(G,x,y):
    n = len(G)
    
    def dijkstra():
        nonlocal x,y, n
        parent = [[None for _ in range(2)] for i in range(n)]
        min_dist = [ [float('inf') for _ in range(2)] for i in range(n)]
        q = PriorityQueue()
        q.put((0, x, 0)) # 0 alicja
        q.put((0,x,1)) # 1 bob
        min_dist[x][0] = 0
        min_dist[x][1] = 0
        while not q.empty(): 
            dist, node, driver = q.get()

            if node == y: 
                return dist, driver, parent

            if dist > min_dist[node][driver]: 
                continue 

            for v, w in G[node]:
                new_driver = (driver+1)%2
                if new_driver == 0:
                    if  w + dist < min_dist[v][new_driver]: 
                        min_dist[v][new_driver] = w+dist
                        parent[v][new_driver] = (node, driver)
                        q.put((w+dist, v, new_driver))
                else:
                    if dist < min_dist[v][new_driver]:
                        min_dist[v][new_driver] = dist
                        parent[v][new_driver] = (node, driver)
                        q.put((dist, v, new_driver))

        return -1,-1,-1
    
    cost, driver, parent = dijkstra()
    
    cur_node = y
    cur_driver = driver
    path = []    
    while cur_node is not None:
        path.append(cur_node)
        cur = parent[cur_node][cur_driver]

        if cur == None: break 
        cur_node = cur[0]
        cur_driver = cur[1]
    
    path  = path[::-1]
    print(cost)
    print(path)

if __name__ == "__main__":
    G = [
        [(1, 1), (4, 50)],       # Z miasta 0: do 1 (bardzo tanio) albo do 4 (drogo!)
        [(2, 1)],                # Z miasta 1: do 2 (tanio)
        [(3, 100)],              # Z miasta 2: do 3 (Piekielnie drogo!)
        [],                      # Miasto 3: META
        [(5, 100)],              # Z miasta 4: do 5 (Piekielnie drogo!)
        [(3, 1)]                 # Z miasta 5: do 3 (tanio)
    ]

    start = 0
    koniec = 3
    solve(G,start,koniec)