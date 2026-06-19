def solve(A,n):
    
    def neigh(u):
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        adj = []
        for dr,dc in dir:
            new_r = dr+u[0]
            new_c = dc+u[1]

            if 0 < new_r < n-1 and 0 < new_c < n-1: 
                if A[dr][dc] == 1:
                    adj.append([new_r, new_c])
        return adj