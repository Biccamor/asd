def partition(A,l,r):
    idx = pivot_index(A,l,r) #type:ignore 
    A[idx], A[r] = A[r], A[idx]
    pivot = A[r]
    i = l-1

    for j in range(l,r):
        if A[j] < pivot:
            i+=1
            A[i],A[j] = A[j], A[i]

    A[r], A[i+1] = A[i+1], A[r]

    return i+1

def pivot_index(A, l, r):
    mid = (l + r) // 2
    
    a = A[l]
    b = A[mid]
    c = A[r]
    
    if (b <= a and a <= c) or (c <= a and a <= b):
        return l
        
    elif (a <= b and b <= c) or (c <= b and b <= a):
        return mid

    else:
        return r

def quickselect(A,l,r, k):
    while l<=r: 
        idx = partition(A,l,r)
        if idx == k:
            return A[idx]
        elif idx < k:
            l = idx +1 
        else:
            r = idx -1


A = [1,2,3,432,2,332,34,2,374,37,87]
l = 0
r = len(A)-1
print(quickselect(A,l,r,0))