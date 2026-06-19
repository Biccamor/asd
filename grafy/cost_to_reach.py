import heapq as hq 

def solve(maxTime: int, edges: list, passingFees: list):
    G =[[] for _ in range(len(passingFees))]
    n = len(passingFees)

    for u,v,w in edges:
        G[u].append((v,w))
        G[v].append((u,w))
    
    def dijkstra():
        nonlocal n, maxTime

        min_cost = [ [float('inf')] * (maxTime + 1) for _ in range(n) ]
        min_cost[0][0] = passingFees[0]

        q = []
        hq.heappush(q, (passingFees[0], 0, 0))

        while q: 
            cost, node, time = hq.heappop(q)

            if cost > min_cost[node][time]: continue
            if time > maxTime: continue
            
            if node == n-1: return cost 

            for v, w in G[node]:
                if w+time > maxTime: continue

                if passingFees[v] + min_cost[node][time] < min_cost[v][w+time]:
                    min_cost[v][w+time] = passingFees[v] + min_cost[node][time]
                    hq.heappush(q, (passingFees[v]+min_cost[node][time], v, w+time))
        return -1

    cost = dijkstra()
    return cost

if __name__ == "__main__":
    maxTime = 30
    edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
    passingFees = [5,1,2,20,20,3]
    cost =solve(maxTime, edges, passingFees)
    print(cost)