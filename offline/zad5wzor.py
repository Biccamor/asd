import sys

def read_data():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    n = int(next(iterator))
    m = int(next(iterator)) 
    q = int(next(iterator)) 
    d = int(next(iterator)) 
    
    G = [[] for _ in range(n)]
    E = []
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        c = int(next(iterator))
        
        G[u].append((v, c))
        G[v].append((u, c)) 
        E.append((u,v,c))

    queries = []
    for _ in range(q):
        start = int(next(iterator)) - 1
        end = int(next(iterator)) - 1
        queries.append((start, end))
        
    return n, m, q, d, G, queries, E


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


def solve(G, n, m, d, E, a, b) -> bool:

    nodes = [Node(i) for i in range(n)]
     
    E.sort(key = lambda x: x[2])
    A = []
    for m in E: 
        mini = m[2]
        maxi = m[2] + d 
        nodes = [Node(i) for i in range(n)]

        for e in E:
            if mini <= e[2] <= maxi:
                if union(nodes[e[0]], nodes[e[1]]):
                    A.append((e[0], e[1], e[2]))
            else:
                break       
            if find(nodes[a]) == find(nodes[b]): 
                return True 
        
        if find(nodes[a]) == find(nodes[b]):
            return True
    return False

def main(G, n, m, d, queries, E):
    
    for q in queries: 
        a,b = q
        if solve(G,n,m,d,E, a, b) == True: 
            print("TAK")
        else:
            print("NIE")

if __name__ == "__main__": 
    n, m, q, d, G, queries, E = read_data()
    main(G,n,m,d,queries, E)