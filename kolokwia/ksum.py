import copy 
def partition(A,l,r):
    pivot = A[r]

    i = l-1

    for j in range(l,r):

        if A[j]<pivot:
            i+=1
            A[j],A[i] = A[i],A[j]

    A[r],A[i+1]=A[i+1],A[r]
    return i+1

def quickselect(A,l,r,target):
    B = copy.deepcopy(A)
    while l<=r:
        idx = partition(B,l,r)
        if idx==target:
            return B[idx]
        
        elif idx < target:
           l = idx+1
        else:
            r = idx-1
    return B[l]


def solve(A,k,p):
    ans = 0
    i = 0
    j = i+p-1
    n = len(A)
    while j<=n-1:
        
        akt = quickselect(A,i,j,i+p-k)
        print(akt)
        ans += akt
        j+=1
        i+=1

    return ans


if __name__ == "__main__":
    A = [7,9,1,5,8,6,2,12]
    k = 4
    p = 5 
    ans =solve(A,k,p)
    print(ans)