def carPooling(trips, capacity: int) -> bool:
    n = 0
    for _, f, to in trips:
        n = max(to, n, f)
    
    T = [0]*(n+2)

    for num,fro, to in trips:
        T[fro] += num 
        T[to]-=num
    #print(T)

    akt = 0
    for i in T:
        akt += i
        #print(akt)
        if akt > capacity:
            return False
    return True

carPooling([[2,1,5],[3,3,7]], 4)