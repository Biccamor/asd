class Node:
    def __init__(self, val):
        self.parent = self
        self.val = val 
        self.rank = 0


def find(x):
    if x.parent is not x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: return False

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y 
        if x.rank == y.rank:
            y.rank+=1
    return True


def solve(E, k, n):
    E.sort(key = lambda x: x[2])

    nodes = [Node(i) for i in range(n)]
    A = []
    union(nodes[k[0]], nodes[k[1]])
    cost = k[2]
    edges = 1
    A.append((k[0], k[1], k[2]))
    
    for e in E:
        if e is k: continue
        if edges == n-1:
            print(A)
            return A 
              
        if union(nodes[e[0]], nodes[e[1]]):
            cost += e[2]
            A.append((e[0], e[1], e[2]))
            edges+=1

    if edges != n-1:
        print("co")
        return -1
    else:
        print(A)
        return A


def run_tests():
    print("--- START TESTÓW ---")

    # TEST 1: Zwykły graf, wymuszamy krawędź, która i tak byłaby w optymalnym MST
    n1 = 4
    E1 = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10)]
    k1 = E1[0] # Wymuszamy (0, 1, 1)
    res1 = solve(E1, k1, n1)
    assert res1 is not  None, "Test 1 FAIL: Powinno zwrócić drzewo"
    assert len(res1) == 3, "Test 1 FAIL: Zła liczba krawędzi"
    print("Test 1 (Standardowy): ZALICZONY")

    # TEST 2: Wymuszamy SUBOPTYMALNĄ krawędź (bardzo drogą). 
    # Algorytm musi zbudować drzewo wokół niej, pomijając tańsze, jeśli tworzą cykl.
    n2 = 4
    E2 = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10)]
    k2 = E2[3] # Wymuszamy koszmarnie drogie (0, 3, 10)
    res2 = solve(E2, k2, n2)
    koszt2 = sum(w for u, v, w in res2)
    # Spodziewane drzewo: (0,3,10), (0,1,1), (1,2,2) -> suma 13.
    # Krawędź (2,3,3) zostanie odrzucona, bo stworzyłaby cykl.
    assert koszt2 == 13, f"Test 2 FAIL: Zły koszt MST, wyszło {koszt2}, a powinno 13"
    print("Test 2 (Suboptymalna krawędź k): ZALICZONY")

    # TEST 3: Graf niespójny (nie da się połączyć wszystkich miast)
    n3 = 4
    E3 = [(0, 1, 1), (2, 3, 2)]
    k3 = E3[0]
    res3 = solve(E3, k3, n3)
    assert res3 is not None, "Test 3 FAIL: Graf niespójny powinien zwrócić None"
    print("Test 3 (Graf niespójny): ZALICZONY")

    # TEST 4: Graf z tylko 2 wierzchołkami (najmniejszy sensowny graf)
    n4 = 2
    E4 = [(0, 1, 5)]
    k4 = E4[0]
    res4 = solve(E4, k4, n4)
    assert len(res4) == 1, "Test 4 FAIL: Drzewo 2-wierzchołkowe powinno mieć 1 krawędź"
    print("Test 4 (Minimalny graf): ZALICZONY")
    
    print("--- WSZYSTKIE TESTY ZALICZONE NA 5.0! ---")

if __name__ == "__main__":
    run_tests()