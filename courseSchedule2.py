def solve(tab,n):
    G = [[] for _ in range(n)]
    for i in tab:
        G[i[1]].append(i[0])

    states = [0]*n 
    order = []
    def dfs(G,u, states):
        states[u] = 1 

        for v in G[u]: 

            if states[v] == 0: 
                if dfs(G,v, states)==True:
                    return dfs(G, v, states)
            elif states[v] == 1:
                return True 
            
        states[u] = 2
        order.append(u) 
        return False

    for u in range(n):
        if states[u] == 0:
            check = dfs(G,0,states)
            if check == True:
                return []

    return order[::-1]

if __name__ == "__main__":
    n =2
    l = [[1,0]]
    ans = solve(l,n)
    print(ans)