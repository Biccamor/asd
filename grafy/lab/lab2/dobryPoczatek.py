def solve(G,n):
    vis = [False]*n 
    order = []
    def dfs(u): 
        vis[u] = True 
        for v in G[u]:
            if not vis[v]:
                dfs(v)
        order.append(u)
    
    for u in range(n):
        if vis[u] == False:
            dfs(u)

    vis = [False]*n 
    start = order[-1]
    dfs(start)

    for v in vis:
        if v == False:
            return False 
    
    return start 


def run_tests():
    tests = [
        {
            "name": "1. Prosta linia (DAG)",
            "n": 4,
            # 0 -> 1 -> 2 -> 3
            # Tylko z 0 da się dojść wszędzie.
            "edges": [(0, 1), (1, 2), (2, 3)],
            "expected": 0 
        },
        {
            "name": "2. Odwrócona linia (Zaczynamy z końca)",
            "n": 4,
            # 3 -> 2 -> 1 -> 0
            "edges": [(3, 2), (2, 1), (1, 0)],
            "expected": 3
        },
        {
            "name": "3. Dwa źródła (Brak Dobrego Początku)",
            "n": 3,
            # 0 -> 2 oraz 1 -> 2
            # Z 0 nie dojdziesz do 1, z 1 nie dojdziesz do 0.
            "edges": [(0, 2), (1, 2)],
            "expected": False
        },
        {
            "name": "4. Rozłączne wyspy (Brak Dobrego Początku)",
            "n": 4,
            # 0 -> 1 oraz 2 -> 3
            "edges": [(0, 1), (2, 3)],
            "expected": False
        },
        {
            "name": "5. Jeden wielki cykl (Każdy jest dobry)",
            "n": 3,
            # 0 -> 1 -> 2 -> 0
            # Skoro to cykl, dowolny wierzchołek jest "Dobrym Początkiem". 
            # Twój algorytm dla tego układu krawędzi wyłowi wierzchołek 0.
            "edges": [(0, 1), (1, 2), (2, 0)],
            "expected": 0
        },
        {
            "name": "6. Dobry początek prowadzi do cyklu",
            "n": 5,
            # 0 -> 1, a potem cykl 1 -> 2 -> 3 -> 4 -> 1
            # Tylko 0 może być dobrym początkiem (z cyklu nie wrócisz do 0).
            "edges": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)],
            "expected": 0
        },
        {
            "name": "7. Gwiazda (Jedno źródło w centrum)",
            "n": 4,
            # 0 -> 1, 0 -> 2, 0 -> 3
            "edges": [(0, 1), (0, 2), (0, 3)],
            "expected": 0
        }
    ]

    for test in tests:
        G = [[] for _ in range(test["n"])]
        for u, v in test["edges"]:
            G[u].append(v)
            
        wynik = solve(G, test["n"])
        
        status = "✅ PASS" if wynik == test["expected"] else "❌ FAIL"
        print(f"{status} | {test['name']} (Oczekiwano: {test['expected']}, Otrzymano: {wynik})")

if __name__ == '__main__':
    run_tests()