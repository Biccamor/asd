import sys
import array
# def partition(A, l,r):

#     mid = (l + r) // 2
#     if A[l] > A[mid]: A[l], A[mid] = A[mid], A[l]
#     if A[mid] > A[r]: A[mid], A[r] = A[r], A[mid]
#     if A[l] > A[mid]: A[l], A[mid] = A[mid], A[l]
    
#     A[mid], A[r] = A[r], A[mid]
#     pivot = A[r]
    
#     i = l-1
    
#     for j in range(l,r):
#         if A[j] < pivot:
#             i+=1
#             A[j],A[i]=A[i],A[j]
        
#     A[i+1],A[r] = A[r], A[i+1]
#     return i+1

def partition(A,l,r):
    pivot = A[(l+r)//2]

    i,j = l-1, r+1

    while True:
        i+=1
        while A[i] < pivot:
            i+=1
        j-=1
        while A[j]>pivot:
            j-=1

        if i>=j:
            return j
        
        A[i],A[j] = A[j], A[i]

def quickselect(A, l, r, target_idx):

    while l<r:
        idx = partition(A,l,r)

        if idx < target_idx:
            l = idx+1
        else:
            r = idx
    return l

def tokens():
    for line in sys.stdin.buffer:
        yield from line.split()

def main():
    it = tokens()
    n = int(next(it))
    A = array.array('i', (int(next(it)) for _ in range(n)))
    q = int(next(it))
    queries = array.array('i', (int(next(it)) for _ in range(q)))

    out = []
    for k in queries:
        idx = quickselect(A, 0, n - 1, n - k)
        out.append(A[idx])

    sys.stdout.write('\n'.join(map(str, out)) + '\n')

if __name__ == "__main__":
    main()