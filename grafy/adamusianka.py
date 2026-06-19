# swiezo kupiona woda zawsze przejezda 
# kazda minuta to szklanka

import heapq as hp

def abus(KR, OD, b, s, t):
    n = len(OD)
    G = [[] for _ in range(n)]

    for e in KR: 
        G[e[0]].append([e[1], e[2]])
        G[e[1]].append([e[0], e[2]])
    

    def dijkstra():
        nonlocal n, s, t, b

        min_l = [float('inf')]*n 
        min_adamus = [float('inf')]*n
        q = []
        hp.heappush(q, [0, s, b])

        while q: 
            water, node, l = hp.heappop(q)

            if min_l[node] < l or min_adamus[node] < water: 
                continue

            for v, w in G[node]:
                 
