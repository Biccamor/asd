def solve(numCourses, prerequisites):
    g = [[] for _ in range(numCourses)]
    for pair in prerequisites:
        g[pair[1]].append(pair[0])

    stan = [0]*numCourses

    def dfs(G,u, stan):
        stan[u] = 1

        for v in G[u]:
            if stan[v]==0:
                if dfs(G,v,stan)==True:
                    return True

            elif stan[v]==1:
                return True 
        
        stan[u] = 2
        return False
        
    for u in range(numCourses):
        if stan[u] == 0:
            if dfs(g,u,stan) == True:
                return False 
            
    return True 


if __name__ == "__main__":
    num = 2
    g = [[0,1]]
    print(solve(num,g))