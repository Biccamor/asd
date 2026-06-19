from queue import PriorityQueue

def create_graph(E): 
    n = 0 
    for u,v,w in E:
        n = max(n,u,v)
    n+=1
    G =[[] for _ in range(n)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    return G,n


def warrior(E,s,t):
    G,n = create_graph(E)
    def dijkstra():
        nonlocal s,t,n 
        q = PriorityQueue()
        min_hours = [[float('inf') for _ in range(17)] for i in range(n)]
        min_hours[s][16] = 0 
        q.put((0, s,16))
        while not q.empty():
            
            time,node,energy = q.get()

            if node == t: return time

            if time > min_hours[node][energy]:
                continue
            
            q.put((time+8, node, 16))

            for v, w in G[node]: 
                if energy - w > 0:
                    if time + w < min_hours[v][energy-w]: 
                        min_hours[v][energy-w] = time + w 
                        q.put((time+w,v,energy-w))
    time = dijkstra()
    print(time)

if __name__ == "__main__":
    G = [ (1,5,10), (4,6,12), (3,2,8),
    (2,4,4) , (2,0,10), (1,4,5),
    (1,0,6) , (5,6,8) , (6,3,9)]
    s = 0
    t = 6
    warrior(G,s,t)