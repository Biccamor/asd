def merge(A,B,rank,p,q,r):
    i = p
    j = q
    k = p

    while i<q and j<r:

        if A[i][0] <= A[j][0]:
            B[k] = A[i]
            k+=1 
            i+=1
        else:
            B[k] = A[j]
            rank[A[j][1]] += i-p
            k+=1
            j+=1
    while i<q:
        B[k] = A[i]
        k+=1
        i+=1

    while j<r:
        B[k] = A[j]
        rank[A[j][1]] += i-p
        k+=1
        j+=1 

    for t in range(p,r):
        A[t] = B[t]


def merge_sort(A,B,rank,p,r):
    
    if r-p <= 1: return
    
    q = (p+r)//2
    
    merge_sort(A,B,rank,p,q)
    merge_sort(A,B,rank,q,r)

    merge(A,B,rank,p,q,r)

def solve(T):
    
    for i in range(len(T)):
        T[i] = [T[i], i]
    B = [[0,0] for _ in range(len(T))]
    rank = [0]*len(T)
    merge_sort(T,B,rank,0,len(T))
    print(rank)
    
if __name__=="__main__":
    T = [5, 4, 3, 2, 1]
    solve(T)