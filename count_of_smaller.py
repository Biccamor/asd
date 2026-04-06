def merge(A, B,dom, p,q,r):
    i = p
    j = q
    k = p

    while i<q and j<r:

        if A[i][0] <= A[j][0]:
            B[k] = A[i]
            dom[A[i][1]] += j-q

            i+=1
            k+=1
        else:
            B[k] = A[j]
            j+=1
            k+=1
    
    while i<q:
        B[k] = A[i]
        dom[A[i][1]] += j-q
        i+=1
        k+=1

    while j<r:
        B[k] = A[j]
        j+=1
        k+=1
    
    for t in range(p,r):
        A[t] = B[t]
    

def merge_sort(A,B,dom,p,r):
    if r-p<=1: return
    q = (p+r)//2

    merge_sort(A,B,dom,p,q)
    merge_sort(A,B,dom,q,r)
    merge(A,B,dom,p,q,r)


def solve(A):
    
    n = len(A)
    B = [0]*n

    for i in range(n):
        A[i] = [A[i], i]

    dom = [0]*n

    merge_sort(A,B,dom,0,n)
    return dom



if __name__ == "__main__":
    nums = [5,2,6,1]
    dom = solve(nums)
    print(dom)
