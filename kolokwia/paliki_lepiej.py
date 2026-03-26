def insertio_sort():
    ...

def solve(T,M,D):
    ile = M/len(T)
    bucket = [[] for _ in range(len(T))]

    for el in T:

        idx = int(el/ile)
        bucket[idx].append(el)
    
    for els in bucket:
        els.sort()
    
    prev = None
    ans = 0 
    for lista in bucket:
        for el in lista:
            
            if prev == None:
                prev = el
                continue
            
            if el - prev >= D: 
                ans += 1
            prev = el
    
    return ans

if __name__ == "__main__":
    M = 10
    D = 0.9
    T = [3.55, 7.12, 1.3, 0.6, 9.4]
    ans = solve(T,M,D)
    print(ans)