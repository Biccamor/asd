"""
Chcemy znalezc takie A[i]-A[j] ktore w posortowanej talbicy byloby najwieksze jedna A jest nie posortwane
i dostepne mamy O(n) czasu"""

def solve(A):
    n = len(A)
    maxi = max(A)
    mini = min(A)
    if maxi == mini: return 0

    d = (maxi-mini)//(n) +1

    bucket_min = [float("inf")]*(n+1)
    bucket_max = [float("-inf")]*(n+1)
    #print(f"n: {n}, d: {d}, maxi-mini {maxi-mini}")
    
    for i in range(n):
        akt = A[i]
        idx = (akt-mini)//d
        bucket_max[idx] = max(bucket_max[idx], akt)
        bucket_min[idx] = min(bucket_min[idx], akt)
    prev = bucket_max[0] 
    i = 1
    while prev == float("-inf"):
        prev = bucket_max[i]
        i+=1
    ans = 0
    for i in range(1,len(bucket_max)):
        
        akt = bucket_min[i]
        if akt == float("inf"):
            continue
        ans = max(akt-prev, ans)
        prev = bucket_max[i]
    return ans


if __name__ == "__main__":
    A = [1,4,12,3,7,17,8,20,26,13,34,30,70,65,5,44]
    print(solve(A))