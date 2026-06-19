from math import sqrt, ceil

class Node: 
    def __init__(self, val):
        self.parent = self
        self.val = val 
        self.rank = 0


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent 

def union(x,y): 
    x = find(x)
    y = find(y)

    if x==y: return False 

    if x.rank > y.rank:
        y.parent = x 
    else:
        x.parent = y 
        if y.rank == x.rank:
            y.rank+=1

    return True


def solve(miasta,N):
    """
    E = ((x1,y1, x2,y2)) czyli z punktu x1,y1 krawedz do x2,y2""" 
    edges = []

    for i in range(N):
        for j in range(i + 1, N): # (i + 1), żeby nie łączyć miasta samego ze sobą i nie dublować krawędzi
            
            x1, y1 = miasta[i]
            x2, y2 = miasta[j]
            
            dystans = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            waga = ceil(dystans)
            
            edges.append((i, j, waga))

    edges.sort(key=lambda x: x[2])
    min_dif = [float('inf'), -1, -1]
    for x in edges:
        akt_min = x[2]
        nodes = [Node(i) for i in range(N+1)]
        maxi = akt_min
        edges_num = 0
        for e in edges:

            if  e[2] >= akt_min and union(nodes[e[0]], nodes[e[1]]):
                maxi = max(maxi, e[2])
                edges_num+=1
                if edges_num == N-1:
                    if maxi - akt_min < min_dif[0]:
                        min_dif = [maxi-akt_min, akt_min, maxi]
                    break

        if edges_num == N-1:
            if maxi - akt_min < min_dif[0]:
                min_dif = [maxi-akt_min, akt_min, maxi]
                
    return min_dif

if __name__ == "__main__":
    miasta = [
    (0, 0),   # Miasto 0
    (0, 1),   # Miasto 1
    (10, 0),  # Miasto 2
    (10, 1)   # Miasto 3
    ]
    N = 4
    min_dif = solve(miasta, N)
    print(min_dif)