from queue import PriorityQueue
import math 

def solve(G,k,n,src,dst):
    path = []
    parent = [None]*n
    vis = [False]*n
    def dijkstra():
        nonlocal src, dst

        queue = PriorityQueue()
        queue.put([float('-inf'),src])
        while not queue.empty(): 
            c, u = queue.get()         

            if vis[u] == True: continue 
            
            vis[u] = True

            if u == dst:
                return -c

            for v in G[u]:
                if not vis[0]:
                    queue.put([-min(-c, v[1]), v[0]])
        return -1 
    
    c = dijkstra()
    if c == -1: return -1,-1
    groups = math.ceil(k/c)
    
    curr = dst 
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    return groups, path[::-1]

def run_tests():
    tests = [
        {
            "name": "1. Prosta sciezka (idealne dzielenie)",
            "n": 3, "k": 30, "src": 0, "dst": 2,
            "edges": [[0, 1, 10], [1, 2, 20]],
            "expected_c": 10,       # Wąskie gardło to 10
            "expected_groups": 3    # 30 turystów / 10 = 3
        },
        {
            "name": "2. Prosta sciezka (reszta z dzielenia)",
            "n": 3, "k": 31, "src": 0, "dst": 2,
            "edges": [[0, 1, 10], [1, 2, 20]],
            "expected_c": 10,       
            "expected_groups": 4    # 31 / 10 = 3.1 -> potrzebujemy 4 grupek
        },
        {
            "name": "3. Dwie drogi, wybieramy szersza",
            "n": 4, "k": 100, "src": 0, "dst": 3,
            "edges": [
                [0, 1, 50], [1, 3, 40], # Trasa górna: gardło 40
                [0, 2, 30], [2, 3, 30]  # Trasa dolna: gardło 30
            ],
            "expected_c": 40,
            "expected_groups": 3    # 100 / 40 = 2.5 -> 3 grupki
        },
        {
            "name": "4. Bezposrednia vs Okrezna",
            "n": 4, "k": 50, "src": 0, "dst": 3,
            "edges": [
                [0, 3, 10],             # Bezpośrednia droga jest bardzo wąska (gardło 10)
                [0, 1, 100], [1, 2, 80], [2, 3, 60] # Okrężna jest super szeroka (gardło 60)
            ],
            "expected_c": 60,
            "expected_groups": 1    # 50 / 60 = 0.83 -> 1 grupka wystarczy!
        },
        {
            "name": "5. Brak polaczenia",
            "n": 3, "k": 10, "src": 0, "dst": 2,
            "edges": [[0, 1, 50]],  # Wierzchołek 2 jest odcięty
            "expected_c": -1,
            "expected_groups": -1
        }
    ]

    for test in tests:
        # Budowanie grafu tak jak u Ciebie
        G = [[] for _ in range(test["n"])]
        for u, v, c in test["edges"]:
            G[u].append([v, c])
            G[v].append([u, c]) # Zakładamy graf nieskierowany (autobusy jeżdżą w obie strony)

        # Uruchomienie Twojej funkcji
        c, groups = solve(G, test["k"], test["n"], test["src"], test["dst"])

        status = "✅ PASS" if c == test["expected_c"] and groups == test["expected_groups"] else "❌ FAIL"
        print(f"{status} | {test['name']}")
        if status == "❌ FAIL":
            print(f"   Oczekiwano: gardlo={test['expected_c']}, grup={test['expected_groups']}")
            print(f"   Otrzymano:  gardlo={c}, grup={groups}")

run_tests()