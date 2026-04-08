def merge(A,B,p,q,r):
    i = p
    j = q
    k = p

    while i<q and j<r:
        if A[i][1]<=A[j][1]:
            B[k] = A[i]
            i+=1
            k+=1
        else:
            B[k] = A[j]
            j+=1
            k+=1
    
    while i<q:
        B[k] = A[i]
        i+=1
        k+=1
    
    while j<r:
        B[k] = A[j]
        j+=1
        k+=1

    for t in range(p,r):
        A[t] = B[t]

def merge_sort(A,B,p,r):
    if r-p <= 1: return 
    
    q = (p+r)//2 

    merge_sort(A,B,p,q)
    merge_sort(A,B,q,r)

    merge(A,B,p,q,r)


def solve(T):
    for i, el in enumerate(T):
        mini_el = min(el, el[::-1])
        T[i] =[mini_el, hash(mini_el)]

    B = [[0,0] for _ in range(len(T))]
    merge_sort(T,B,0,len(T))
    prev = T[0][0]
    ans = 0
    akt = 1 
    for el in T[1:]:
        if el[0] == prev: 
            akt += 1
        else:
            ans = max(akt, ans)
            akt = 1
            prev = el[0]
    ans = max(akt,ans)
    return ans 


if __name__=="__main__":
    T = ["pies", "mysz","kot", "kogut","tok","seip", "kot"]
    ans = solve(T)
    print(ans)