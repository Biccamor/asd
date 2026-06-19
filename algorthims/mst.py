class Node:
    def __init__(self, val) -> None:
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
            y.rank +=1
    return True 

def mst(E):
    E.sort(key = lambda x: x[2])
    
    n = 0
    for i in E:
        n = max(n, i[0], i[1])
    n = n+1
    nodes = [Node(i) for i in range(n)]
    A = []
    cost = 0 
    edges = 0
    for e in E:
        if union(nodes[e[0]], nodes[e[1]]):
            cost += e[2]
            A.append((e[0], e[1], e[2]))
            edges +=1 
            if edges == n-1:
                break 
    
    if edges != n-1: 
        return -1
    
    return cost 


if __name__ == "__main__":
    # Test (waga na końcu: u, v, waga)
    krawedzie = [
        (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)
    ]
    print("Koszt MST:", mst(krawedzie)) # Zwróci 16