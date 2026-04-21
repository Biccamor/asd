from queue import PriorityQueue

def solve(G, price, d, src, dst, n):

    min_cost = [ [ float('inf') for _ in range(d+1)] for _ in range(n) ]
    parent= [[(None, None) for _ in range(d+1)] for _ in range(n)] # poprzedni wierzcholek, stan wczesniejszy baku


    def dijkstra():
        nonlocal d, src, dst, parent, min_cost
        queue = PriorityQueue()
        queue.put([0, src, 0])

        while not queue.empty():
            cost, node, akt_d= queue.get()

            if node == dst: return cost, akt_d
            if cost > min_cost[node][akt_d]: continue

            if akt_d < d:
                n_cost = cost + price[node]
                n_d = akt_d + 1 
            
                if n_cost < min_cost[node][n_d]:
                    queue.put([n_cost, node, n_d])
                    min_cost[node][n_d] = n_cost  
                    parent[node][n_d] = [node, akt_d]

            for v in G[node]: 
                
                if v[1] <= akt_d:
                    if min_cost[v[0]][akt_d-v[1]] > cost: 
                        
                        min_cost[v[0]][akt_d-v[1]] = cost 
                        parent[v[0]][akt_d-v[1]] = [node, akt_d]
                        queue.put([cost, v[0], akt_d-v[1]])
        return -1, -1

    cost, akt_d = dijkstra()
    if cost == -1: return -1
    cur = dst 
    path = []
    while cur != src:
        if not path or path[-1] != cur:
            path.append(cur)
        cur, akt_d = parent[cur][akt_d]
    path.append(cur)

    print(path[::-1])
    return cost


def run_tests():
    tests = [
        {
            "name": "1. Tankuj po drodze (Tani sasiad)",
            "n": 3, "src": 0, "dst": 2, "capacity": 10,
            "prices": [10, 1, 10], # Paliwo w miescie 0 to koszmar, w 1 to promocja
            "edges": [[0, 1, 2], [1, 2, 8]], # Dystans 0->1 to 2km, 1->2 to 8km
            # Strategia: Tankujemy 2 litry w (0) za 20zl. Jedziemy do (1). Tankujemy 8 litrow za 8zl. Jedziemy do (2).
            # Razem: 28 zl
            "expected": 28
        },
        {
            "name": "2. Tankuj do pelna na starcie",
            "n": 3, "src": 0, "dst": 2, "capacity": 10,
            "prices": [1, 10, 10], # Na starcie taniocha, dalej drozyzna
            "edges": [[0, 1, 5], [1, 2, 5]], 
            # Strategia: Tankujemy 10 litrow na starcie za 10zl. Przejezdzamy cala trase bez tankowania.
            "expected": 10
        },
        {
            "name": "3. Bak za maly na najdluzsza krawedz",
            "n": 2, "src": 0, "dst": 1, "capacity": 5, # Bak ma 5 litrow
            "prices": [1, 1],
            "edges": [[0, 1, 10]], # Trasa ma 10 km
            "expected": -1 # Nie dojedziemy
        },
        {
            "name": "4. Idealna pojemnosc",
            "n": 2, "src": 0, "dst": 1, "capacity": 10,
            "prices": [5, 5],
            "edges": [[0, 1, 10]],
            # Tankujemy 10L po 5zl = 50zl
            "expected": 50
        }
    ]

    for test in tests:
        G = [[] for _ in range(test["n"])]
        for u, v, w in test["edges"]:
            G[u].append([v, w])
            G[v].append([u, w]) # Graf nieskierowany

        wynik = solve(G, test["prices"], test["capacity"], test["src"], test["dst"], test["n"])
        status = "✅ PASS" if wynik == test["expected"] else "❌ FAIL"
        print(f"{status} | {test['name']} (Oczekiwano: {test['expected']}, Otrzymano: {wynik})")

if __name__ == "__main__":
    run_tests()