from queue import PriorityQueue

def warrior(G,s,t):
    n = len(G)

    def dijkstra():
        nonlocal n, G, s, t

        queue = PriorityQueue()
        queue.put([0, s, 16]) 

        min_h = [[ float('inf') for _ in range(17)] for _ in range(n)]

        while not queue.empty():

            count, node, energy = queue.get()
            if node == t: return count
            
            if min_h[node][energy] < count: continue

            for v, w in G[node]: 
                if energy - w >= 0: 
                    if min_h[v][energy-w] > w + count:
                        min_h[v][energy-w] = w+count 
                        queue.put([count+w, v, energy-w])
                else:
                    new_energy = 16 
                    if min_h[v][new_energy-w] > w + count + 8: 
                        min_h[v][new_energy-w] = w +count+8 
                        queue.put([count+8+w, v, new_energy-w])

    ans = dijkstra()
    return ans 

import unittest

# Zakładamy, że funkcja warrior przyjmuje już ZBUDOWANĄ listę sąsiedztwa G
# zadeklarowaną np. tak: G = [[(sasiad, waga), ...], ...]

def build_graph(edges):
    n = 0
    for u, v, w in edges:
        n = max(n, u, v)
    n += 1
    G = [[] for _ in range(n)]
    for u, v, w in edges:
        G[u].append((v, w))
        G[v].append((u, w))
    return G

class TestWarrior(unittest.TestCase):

    def test_zmutowana_energia(self):
        # Trasa 0 -> 1 -> 3 powinna kosztować 10 + 2 = 12 bez snu.
        # Ale jeśli algorytm najpierw sprawdzi drogę do 2 (gdzie trzeba spać),
        # zmutuje sobie energię na 16 i doliczy czas +8 ZANIM sprawdzi drogę do 3!
        edges = [(0, 1, 10), (1, 2, 10), (1, 3, 2)]
        G = build_graph(edges)
        
        # Prawdziwy wynik to 12. 
        # Twój STARY kod wyrzuci 20 (bo doliczy sen dla sąsiada 3, wymuszony przez sąsiada 2!)
        self.assertEqual(warrior(G, 0, 3), 12)
    def test_przyklad_z_tresci(self):
        edges = [(1,5,10), (4,6,12), (3,2,8), (2,4,4), (2,0,10), (1,4,5), (1,0,6), (5,6,8), (6,3,9)]
        G = build_graph(edges)
        # Oczekiwany: 0 -> 1 (6h) -> 4 (5h) [SEN +8h] -> 6 (12h) = 6 + 5 + 8 + 12 = 31
        self.assertEqual(warrior(G, 0, 6), 31)

    def test_krotka_trasa_bez_snu(self):
        edges = [(0, 1, 5), (1, 2, 5)]
        G = build_graph(edges)
        # Oczekiwany: 0 -> 1 (5) -> 2 (5) = 10. (Zostaje 6 energii, brak snu)
        self.assertEqual(warrior(G, 0, 2), 10)

    def test_wymuszony_sen_w_polowie(self):
        edges = [(0, 1, 10), (1, 2, 10)]
        G = build_graph(edges)
        # Oczekiwany: 0 -> 1 (10). Zostaje 6 energii. 
        # Do 2 brakuje 10. Sen w 1 (+8h). 1 -> 2 (10). 
        # Czas: 10 + 8 + 10 = 28
        self.assertEqual(warrior(G, 0, 2), 28)

    def test_sen_na_styk(self):
        edges = [(0, 1, 16), (1, 2, 16)]
        G = build_graph(edges)
        # 0 -> 1 (16). Energia 0. Sen w 1 (+8h). 1 -> 2 (16).
        # Czas: 16 + 8 + 16 = 40
        self.assertEqual(warrior(G, 0, 2), 40)

if __name__ == '__main__':
    unittest.main()