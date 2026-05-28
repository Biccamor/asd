def terminy(T):
    n = 0
    for i in T:
        n = max(i[0], n)
    
    time = [-1]*(n)
    ans = []
    T.sort(key=lambda x: -x[1])

    for d, g in T:
        for j in range(d-1, -1, -1):
            if time[j]==-1:
                time[j] = g
                ans.append((d,g))
                break 
    print(time)
    return sum(time), ans

T = [[2,100], [1,19], [2,27], [1,25], [3,15]]
ans = terminy(T)
print(ans)