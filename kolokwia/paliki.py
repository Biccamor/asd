#   [0.6, 1.5), [1.5, 2.4), [3.3, 4.1), [4.1, 5.0), [5.0, 5.9), [5.9, 6.8), [6.8, 7.6) [7.6, 7.12)

def solve(m,d,T):
    start = min(T)
    maxi = max(T)   
    ilosc = int((maxi-start)/d)+1
    MAXI = 100000000000
    MINI = -1
    min_buckets = [MAXI]*(ilosc)
    max_buckets = [MINI]*(ilosc)
    for el in T:
        idx = int((el - start) // d) 
        if el < min_buckets[idx]:
            min_buckets[idx] = el
        if el > max_buckets[idx]:
            max_buckets[idx] = el
    idx = 0
    while max_buckets[idx] == MINI  :
        idx += 1
    prev = max_buckets[idx]
    ans = 0
    for i in range(len(min_buckets)):
        if min_buckets[i] == MAXI or max_buckets[i] == MINI:
            continue
        if min_buckets[i] - prev > d:
            ans +=1 
        prev = max_buckets[i]

    return ans 

if __name__ == "__main__":
    M = 10
    D = 0.9
    T = [3.55, 7.12, 1.3, 0.6]
    ans = solve(M,D,T)
    print(ans)