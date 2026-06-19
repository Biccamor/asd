from queue import PriorityQueue

def solve(G, k, A, B):
    
    n = len(G)

    def dijkstra():
        nonlocal A, B, k  

        max_pass = [0]*n
        max_pass[A] = k 
        q = PriorityQueue()
        q.put((-k, A))

        while not q.empty(): 
            pas, node = q.get()
            pas = -pas 
            
            if node == B: 
                return pas 

            if max_pass[node] > pas: 
                continue 
            
            for v, c in G[node]: 
                akt_c = min(c,pas)
                if max_pass[v] < akt_c: 
                    max_pass[v] = akt_c
                    q.put((-akt_c, v))
                
    c = dijkstra()

    ile = k / c 

    if int(ile) != ile:
        ile = int(ile)+1
    else:
        ile = int(ile)

    print(ile)
