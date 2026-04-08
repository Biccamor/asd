def insertionSort(arr):
    n = len(arr)
    
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]         
        j = i - 1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key      

def partition(A, l, r):
    pivot = A[r]
    i=l-1
    for j in range(l,r):
        if A[j] < pivot:
            i+=1 
            A[i],A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1

def quickselect(A,k,l,r):
    idx = l
    while l<=r:
        idx = partition(A,l,r)

        if idx == k:
            return idx
        if idx<k:
            l = idx+1
        else:
            r = idx -1 
    return idx
        


def solve(M,D,T):
    n = len(T)

    median = (n//2)
    p = quickselect(T,median,0,n-1)

    small= [[] for _ in range(n//2)]
    big = [[] for _ in range(n//2)]

    for i in range(0, len(small)):
        idx = min(len(small)-1, int((T[i]/T[p]) * (len(small))))
        small[idx].append(T[i])
    
    for i in range(len(small),len(T)):
        idx = min(len(big)-1, int((T[i]-T[p])/(M-T[p])*len(big)))
        big[idx].append(T[i])

    for b in small:
        insertionSort(b)

    for b in big:
        insertionSort(b)
    flatsmall = []
    for b in small:
        flatsmall.extend(b)
    flatbig = []
    for b in big:
        flatbig.extend(b)
    
    sort_T = flatsmall+ flatbig
    ans = 0
    prev = sort_T[0]
    for i in sort_T[1:]:
        if i - prev >= D:
            ans += 1
        prev = i
    print(ans)
if __name__ == "__main__":
    M = 10
    D = 0.9
    T = [3.55, 7.12, 1.3,0.6]
    solve(M,D,T)