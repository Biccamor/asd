def merge(A,B,p,q,r):
    ans =0 
    # wiemy ze lewa czesc tablicy i prawa jest posortowana przykladowo 
    #
    # 1 3 5 7 10 11 | 2 4 6 8 9 12
    # 
    j = q
    for i in range(p,q):
        
        while j < r and A[i] > A[j] *2:
            j+=1
        ans += (j-q)
        

    i = p
    j = q
    k = p
    while i<q and j<r:

        if A[i] <= A[j]:
            
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

    return ans

def merge_sort(A, B, p, r):
    ans = 0
    if r-p <= 1: return 0
    q = (p+r)//2
    ans += merge_sort(A,B,p,q)
    ans += merge_sort(A,B,q,r)
    ans += merge(A,B,p,q,r)
    return ans 
def main(nums):

    n = len(nums)
    B = [0]*n
    ans = 0
    ans = merge_sort(nums,B,0,n)
    print(ans)

if __name__ == "__main__":
    nums = [1,3,2,3,1]
    
    main(nums)
    print(nums)