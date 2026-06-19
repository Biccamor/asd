def solve(G):
    n = len(G)
    vis = [False]*n
    order = []

    def dfs(u):
        vis[u] = True 
        for v in G[u]:
            if vis[v]==False:
                dfs(v)
        order.append(u)

    for u in range(n):
        if vis[u]==False:
            dfs(u)

    order = order[::-1]
    prev = order[0]
    found = False
    for u in order[1:]:
        found = False
        for v in G[prev]:
            if v == u:
                found = True
                continue
        if found == False:
            return False 
        prev = u 
    return True


if __name__ == "__main__":
    # V = 5 (wierzchołki od 0 do 4)
    G_pozytywny = [
        [1, 2, 3],  # z 0 idziemy do 1, 2, 3
        [2, 3, 4],  # z 1 idziemy do 2, 3, 4
        [3, 4],     # z 2 idziemy do 3, 4
        [4],        # z 3 idziemy do 4
        []          # z 4 nigdzie (meta)
    ]
# Ścieżka Hamiltona: 0 -> 1 -> 2 -> 3 -> 4
    ans = solve(G_pozytywny)
    print(ans)