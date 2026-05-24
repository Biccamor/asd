def terminy(T):
    
    T.sort(key = lambda x: (x[0], -x[1]))
    t = 0 
    ans = 0
    for d,g in T:
        if d > t: 
            ans += g 
            t+=1

    print(ans)