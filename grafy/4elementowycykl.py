"""chcemy znalezc 4 elementowy cykl w grafie, reprezentacja macierzowa"""

def solve(G,n):
    
    for a in range(n):
        row = G[a]
        for b in range(a+1, n):
            row2 = G[b]
            akt = 0
            for i in range(n):
                if row[i] == row2[i] == 1:
                    akt+=1
                if akt == 2:
                    return True 
    return False

if __name__ == "__main__":
    g = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]

    ans = solve(g, len(g))
    print(ans)