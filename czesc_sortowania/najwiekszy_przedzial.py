def merge(A,B,intervals,idx,p,q,r):
    i = p
    j = q
    k = p

    while i<q and j<r:

        if A[i][idx] < A[j][idx]:
            B[k] = A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1

        k+=1


def merge_count(A,B,max_interval,p,q,r):
    ...

def merge_sort(A,max_interval, p,r):
    if r-p == 1: return 1
    if r-p < 1: return 0
    
    n = len(A)
    B = [0]*n
    q = (p+r)//2

    merge_sort(A,)    
    merge(A,B,p,r)
