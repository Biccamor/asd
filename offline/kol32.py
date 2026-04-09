def partition(A,l,r):
    pivot = A[r]
    i = l-1
    
    for j in range(l,r):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r], A[i+1] = A[i+1], A[r]

    return i+1

def quickselect(A,l,r,k) -> int | None:

    while l<=r:
        idx = partition(A,l,r)

        if idx == k:
            return A[idx]
        elif idx < k:
            l = idx + 1 
        else:
            r = idx -1 

    return 

def solve(T,k,p):
    
    l = 0
    h = p-1
    n = len(T)
    ans = 0 
    while h<n:
        B = T[l:h+1] # <---> To jest O(p) nie uzywaj full copy bo to jest wtedy O(N) bo tyle ile elementow kopiujesz taka jest zlozonosc uwazaj na to 
        akt = quickselect(B,0,p-1,p-k) # # PAMIETAJ JEZELI JEST SLIDING WINDOW TO INDEKS TEZ SIE PRZESUWA
        #print(T)
        #print(akt)
        ans += akt  # type: ignore
        h += 1 
        l += 1
        #print(l,h,n)

    return ans 


if __name__ == "__main__":
    T = [7,9,1,5,8,6,2,12]
    k = 4
    p = 5

    ans =solve(T,k,p)
    print(ans)