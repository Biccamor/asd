from queue import PriorityQueue

def solve(A,B,G,D,P):
    n = len(G)

    def dijkstra():
        nonlocal A,B,n 
        min_cost = [[float('inf') for _ in range(D+1)] for i in range(n)]
        parent = [[float('inf') for _ in range(D+1)] for i in range(n)]
        min_cost[0][0] = 0
        q = PriorityQueue()
        q.put((0,A, 0))

        while not q.empty():
            cost, node, fuel =  q.get()
         
            if cost > min_cost[node][fuel]: continue

            if node == B:
                return cost

            if fuel < D: 
                new_fuel = fuel + 1
                new_cost = cost+ P[node]
                if min_cost[node][new_fuel] > new_cost:
                    q.put((new_cost, node, new_fuel))

            for v,w  in G[node]:
                if fuel < w: continue

                if min_cost[v][fuel-w] > cost:
                    min_cost[v][fuel-w] = cost 
                    q.put((cost, v,fuel-w))

    cost = dijkstra()
    return cost


if __name__ == "__main__":
    N = 4           # Liczba miast (0, 1, 2, 3)
    MAX_BAK = 3     # Maksymalna pojemność baku (w litrach)
    START = 0       # Zaczynamy w mieście 0
    META = 3        # Chcemy dojechać do miasta 3

    # Ceny paliwa w poszczególnych miastach (zł/litr):
    # Miasto 0: 5 zł (Drogo)
    # Miasto 1: 1 zł (Oaza taniości!)
    # Miasto 2: 8 zł (Zdzierstwo)
    # Miasto 3: 0 zł (Meta, nie musimy już tankować)
    ceny = [5, 1, 8, 0] 

    # Mapa dróg: (miasto_A, miasto_B, dystans_w_km)
    krawedzie = [
        (0, 1, 2),  # Z 0 do 1 jest 2 km
        (1, 3, 2),  # Z 1 do 3 jest 2 km
        (0, 2, 1),  # Z 0 do 2 jest 1 km (Krótka trasa!)
        (2, 3, 2)   # Z 2 do 3 jest 2 km
    ]

    G = [[] for _ in range(N)]

    for u,v,w in krawedzie:
        G[u].append((v,w))
        G[v].append((u,w))
    
    cena = solve(START, META, G, MAX_BAK, ceny)
    print(cena)