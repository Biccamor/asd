from queue import PriorityQueue


def lets_roll(start, flights, resorts):

    n = 0 
    for i in flights:
        n  = max(n, i[1], i[0])
    
    G = [[] for _ in range(n+1)]

    for v in flights:
        G[v[0]].append([v[1], v[2]])
        G[v[1]].append([v[0], v[2]])
    vis = [False]*(n+1)
    print(G)
    def dijkstra(src):
        nonlocal n

        min_cost = [float('inf')]*(n+1)
        min_cost[0] = 0
        queue = PriorityQueue()
        queue.put([0,src])

        while not queue.empty():

            cost, node = queue.get()

            if min_cost[node] < cost: continue

            for v,w in G[node]:
                if vis[v] == True: continue

                if min_cost[v] > cost + w: 
                    min_cost[v] = cost+w 
                    queue.put([cost+w, v])
        return min_cost
    
    ans = 0
    for _ in range(len(resorts)): 

        min_cost = dijkstra(start)
        cost = [float('inf'), -1]
        for r in resorts:
            if min_cost[r] < cost[0]:
                cost = [min_cost[r], r]

        ans += cost[0]*2
        vis[cost[1]] = True 

    return ans 


if __name__ == "__main__":
    start_city = 0
    flights = [(0, 1, 2), (0, 2, 4), (0, 3, 8),
    (3, 4, 16), (1, 4, 1), (2, 4, 1)]
    resorts = [1, 2, 4] 
    ans = lets_roll(start_city, flights, resorts)
    print(ans)