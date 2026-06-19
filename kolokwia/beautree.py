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

    if x==y: return False 

    if x.rank > y.rank:
        y.parent = x
    
    else: 
        x.parent = y
        if x.rank == y.rank: 
            y.rank+=1 
    return True


def beautree(G):
    n = len(G)

    cost = 0
    A = []
    E = []
    for u, neighbors in enumerate(G):
        for v, w in neighbors:
            if u < v: 
                E.append((u, v, w))
    E.sort(key = lambda x: x[2])

    
    n_E = len(E)
    for m in range(n_E- n +2): # E razy okolo dokladnie E-V-1
        is_tree = True
        cost = 0
        branch = 0
        nodes = [Node(i) for i in range(n)]

        for v in range(m, m+n-1): # V-1 razy
            if union(nodes[E[v][0]], nodes[E[v][1]]) == False:
                is_tree = False 
                break 
            else:
                branch+=1
                cost += E[v][2]
                if branch == n-1: break
            
        if branch == n-1 and is_tree == True:
            return cost
    return -1 

if __name__ == "__main__": 
    G = [ [(1,3), (2,1), (4,2)], # 0
        [(0,3), (2,5) ], # 1
        [(1,5), (0,1), (3,6)], # 2
        [(2,6), (4,4) ], # 3
        [(3,4), (0,2) ] ] # 4
    cost = beautree(G)
    print(cost)