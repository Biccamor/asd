from queue import PriorityQueue

def solve(n, f, src, dst, k):
    G = [[] for _ in range(n+1)]

    for (a,b,price) in f:
        G[a].append([b,price])
    print(G)
    def dijkstra():
        nonlocal G, src,dst, k

        queue = PriorityQueue()
        queue.put([0,src, 0])
        min_steps = [float('inf')]*n 
        min_steps[src] = 0 

        while queue.empty() is False: 

            act= queue.get()
            dist = act[0]
            node = act[1]
            steps = act[2]

            if steps > k+1: continue
            
            if node == dst: 
                return dist

            if len(G[node]) == 0: continue
            
            if min_steps[node] < steps: continue
            
            min_steps[node] = steps
            for v in G[node]: 
                
                queue.put([dist+v[1], v[0], steps+1])
        return -1
    
    cost = dijkstra()
    return cost 

if __name__ == "__main__":
    n = 4 
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    cost = solve(n,flights,src,dst,k)
    print(cost)