def bit(T):
    stos = []
    n = len(T)
    stos.append(T[0])
    for i in range(1,n):
        
        if T[i] < stos[-1]: 
            stos.append(T[i])
            continue
        while True:
            akt = stos.pop()
            if akt > T[i]: 
                stos.append(akt)
                break 
            if len(stos)==0:
                break
    print(stos) 
    return len(stos)

T=[5,4,3,2,4,3,1]

print(bit(T))
                