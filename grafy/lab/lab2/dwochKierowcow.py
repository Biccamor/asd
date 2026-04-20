from queue import PriorityQueue

def solve(G,src,dst,n):
    dist = [[float('inf'), float('inf')] for _ in range(n)]
    parent = [[None, None] for _ in range(n)]

    def dijkstra():
        nonlocal src, dst
        dist[src][0] = 0 
        dist[src][1] = 0
        queue = PriorityQueue()
        # 0 to Ala 1 to Bob
        queue.put([0,src,0])
        queue.put([0,src,1])

        while not queue.empty():

            d, node, who = queue.get()  
            
            if node == dst:
                return

            for v in G[node]:
                
                if who == 0 and v[1] + d < dist[v[0]][1]: 
                    queue.put([v[1]+d, v[0], 1])
                    dist[v[0]][1] = v[1]+d
                    parent[v[0]][1]= node
                
                elif who == 1 and d <= dist[v[0]][0]:
                    queue.put([d,v[0], 0])
                    dist[v[0]][0] = d
                    parent[v[0]][0] = node
    dijkstra()

    print(parent)
    
    if dist[dst][0] < dist[dst][1]: end = 0
    else: end = 1

    curr = [dst,end]
    path = []
    
    while curr[0] != src:
        path.append(curr[0])
        
        curr = [parent[curr[0]][curr[1]], (curr[1]+1)%2]
    print(path[::-1])
    if curr[1] == 0: 
        print('Ala')
    else:
        print('Bob')
    return min(dist[dst][0], dist[dst][1])

def run_tests():
    tests = [
        {
            "name": "1. Prosta sciezka",
            "n": 3, "src": 0, "dst": 2,
            "edges": [[0, 1, 10], [1, 2, 20]],
            # Opcja 1: Ala(10) -> Bob(20) = Ala przejechala 10
            # Opcja 2: Bob(10) -> Ala(20) = Ala przejechala 20
            # Minimum dla Ali to 10.
            "expected": 10
        },
        {
            "name": "2. Bob bierze najdluzsza krawedz",
            "n": 4, "src": 0, "dst": 3,
            "edges": [[0, 1, 5], [1, 2, 100], [2, 3, 5]],
            # Opcja: Ala(5) -> Bob(100) -> Ala(5) = Ala jedzie 10.
            "expected": 10
        },
        {
            "name": "3. Bezposrednia vs Okrezna",
            "n": 4, "src": 0, "dst": 3,
            "edges": [
                [0, 3, 50],             
                [0, 1, 10], [1, 2, 10], [2, 3, 10] 
            ],
            # Najlepsza opcja: Bob prowadzi od razu z 0 do 3 (koszt 50 spada na niego). Ala jedzie 0!
            "expected": 0
        },
        {
            "name": "4. Slepy zaulek i powrot (test na tablice visited)",
            "n": 4, "src": 0, "dst": 3,
            "edges": [
                [0, 1, 10], [1, 2, 5], [2, 1, 5], [1, 3, 10]
            ],
            # Ala(10) -> Bob(10) = 10
            "expected": 10
        }
    ]

    for test in tests:
        G = [[] for _ in range(test["n"])]
        # Graf nieskierowany
        for u, v, c in test["edges"]:
            G[u].append([v, c])
            G[v].append([u, c])

        wynik = solve(G, test["src"], test["dst"], test["n"])

        status = "✅ PASS" if wynik == test["expected"] else "❌ FAIL"
        print(f"{status} | {test['name']}")
        if status == "❌ FAIL":
            print(f"   Oczekiwano: {test['expected']}, Otrzymano: {wynik}")

if __name__ == "__main__":
    run_tests()