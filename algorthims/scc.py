def scc(G,n): 

    order = []
    vis = [False]*n 

    def dfs(u):
        nonlocal G
        vis[u] = True 

        for v in G[u]: 
            if vis[v] == False: 
                dfs(v)

        order.append(u)
    
    for v in range(n):
        if vis[v] == False:
            dfs(v)
    
    G_reverse = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G_reverse[v].append(u)
    
    vis = [False]*n
    

    def dfs_reverse(u):
        nonlocal G_reverse
        vis[u] = True 
        for v in G_reverse[u]: 
            if vis[v] == False: 
                dfs_reverse(v)
        print(u)

    conected = 0
    order = order[::-1]
    for u in order: 
        if vis[u] == False: 
            dfs_reverse(u)
            conected +=1

    return conected 

def run_tests():
    tests = [
        {
            "name": "1. Jeden wielki cykl (1 SSS)",
            "n": 4,
            # 0->1->2->3->0
            "edges": [(0, 1), (1, 2), (2, 3), (3, 0)],
            "expected": 1
        },
        {
            "name": "2. Dwie osobne wyspy (2 SSS)",
            "n": 6,
            # Wyspa 1: 0->1->2->0
            # Wyspa 2: 3->4->5->3
            "edges": [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)],
            "expected": 2
        },
        {
            "name": "3. DAG (Brak cykli - 4 SSS)",
            "n": 4,
            # Linia prosta: 0->1->2->3
            # Skoro nie ma powrotu, każdy wierzchołek to osobna składowa!
            "edges": [(0, 1), (1, 2), (2, 3)],
            "expected": 4
        },
        {
            "name": "4. Wąskie gardło (Motyw Popularnych Krów)",
            "n": 5,
            # Grupa A: 0 i 1 (0<->1)
            # Grupa B: 2, 3, 4 (2->3->4->2)
            # Wąskie gardło: 1 -> 2 (ale nie da się wrócić do 1!)
            "edges": [(0, 1), (1, 0), (1, 2), (2, 3), (3, 4), (4, 2)],
            "expected": 2
        },
        {
            "name": "5. Samotny wierzcholek",
            "n": 1,
            "edges": [],
            "expected": 1
        }
    ]

    for test in tests:
        G = [[] for _ in range(test["n"])]
        # Zauważ: grafy dla SCC MUSZĄ być SKIEROWANE
        for u, v in test["edges"]:
            G[u].append(v)

        wynik = scc(G, test["n"])
        status = "✅ PASS" if wynik == test["expected"] else "❌ FAIL"
        print(f"{status} | {test['name']} (Oczekiwano: {test['expected']}, Otrzymano: {wynik})")

if __name__ == "__main__":
    run_tests()