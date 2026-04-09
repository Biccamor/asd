from zad1testy import runtests

def strong_string(T):
    
    def merge(A,B,p,q,r):
        i = p
        j = q
        k = p

        while i<q and j<r:

            if A[i]<=A[j]:
                B[k] = A[i]
                i+=1
                k+=1
            else:
                B[k] = A[j]
                j+=1
                k+=1

        while i<q:
            B[k] = A[i]
            k+=1
            i+=1
        while j<r:
            B[k] = A[j]
            j+=1
            k+=1

        for t in range(p,r):
            A[t] = B[t]

    def merge_sort(A,p,r):
        if r-p <= 1:
            return

        q =(p+r)//2
        B = [0]*len(A)
        merge_sort(A,p,q)
        merge_sort(A,q,r)
        merge(A,B,p,q,r)       

    def solve(A):

        for i in range(len(A)):
            A[i] = min(A[i], A[i][::-1])
        merge_sort(A,0,len(A))
        prev = A[0]
        akt = 1
        ans = 1
        for el in A[1:]:
            if prev == el:
                akt+=1
            else:
                prev = el
                ans = max(akt,ans)
                akt = 1
        return ans     
    ans = solve(T)
    return ans 

runtests( strong_string, all_tests=False )
