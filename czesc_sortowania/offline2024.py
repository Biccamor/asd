def merge(A,B,p,q,r, dom):
    i = p 
    j = q
    k = p

    while i<q and j < r: 

        if A[i][1] >= A[j][1]:
            B[k] = A[j]

            
            dom[A[j][2]] += i-p
            
            j+=1
            k+=1
        else: 
            B[k] = A[i]
            i+=1
            k+=1

    while i<q:
        B[k] = A[i]
        i +=1
        k+=1
    
    while j<r:
        B[k] = A[j]
        dom[A[j][2]] += q-p
        j+=1
        k+=1
    
    for t in range(p,r):
        A[t] = B[t]


def merge_sort(A, B, p, r, dom):

    if r-p < 2: return

    q = (p+r)//2 

    merge_sort(A,B,p,q, dom)
    merge_sort(A,B,q,r, dom)    
    merge(A,B,p,q,r, dom)

def add_idx(A):
    
    for i in range(len(A)):
        A[i] = (A[i][0], A[i][1], i)


def solve(A):
    n = len(A)
    p, r = 0, n 
    add_idx(A)
    A.sort(key=lambda x: x[0])

    B = [(0,0,0)]*n
    dom = [0]*n
    merge_sort(A,B,p,r,dom)

    return max(dom)

if __name__ == "__main__":
    A = [(1,3), (3,4), (4,2), (2,2)]
    print(solve(A))