import heapq as hq

def solve(G,s,w):
    n = len(G)
    
    def dijkstra():
        nonlocal s,w, n 
        dist = [[float('inf') for _ in range(n)] for i in range(2)]
        dist[s][0] = 0
        dist[s][1] = 0
        
        