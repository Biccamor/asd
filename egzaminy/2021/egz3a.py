def snow(T,I):
    s = []
    for a,b in I:
        s.append((a,1))
        s.append((b,-1))

    s.sort(key = lambda x: (x[0], -x[1]))

    ans = 0
    akt = 0 
    
    for t,z in s: 
        akt += z 
        ans = max(akt, ans)

    return ans 

