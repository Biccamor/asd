def warrior(E,s,t):
    n = 0 

    for i in E:
        n = max(i[0], i[1], n)
    n+=1
    
    G =[[] for _ in range(n)]
    last = n
    for u,v,w in E:
        if w == 1:
            G[u].append(v)
            G[v].append(u)
        else:
            cur = u 

            for _ in range(w-1):
                G.append([])
                G[cur].append(last)
                G[last].append(cur)
                cur = last
                last+=1
            
            G[last-1].append(v)
            G[v].append(last-1)

    print(G)

if __name__=="__main__":
    G = [ (1,5,10), (4,6,12), (3,2,8),
    (2,4,4) , (2,0,10), (1,4,5),
    (1,0,6) , (5,6,8) , (6,3,9)]
    s = 0
    t = 6
    warrior(G,s,t)