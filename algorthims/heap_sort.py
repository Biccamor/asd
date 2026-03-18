def parent(i):
    return i//2
def left(i):
    return (2*i)+1
def right(i):
    return 2*i+2

def heapify(A,n,i):
    """
    A tablica/kopiec 
    n - ilosc liczb w tablicy
    i - akutalny element w kopcu ktory chcemy dac na dobre miejsce
    """
    max_int = i
    if left(i) <n and A[left(i)] > A[max_int]:
        max_int = left(i)
    if right(i) < n and A[right(i)] > A[max_int]:
        max_int = right(i)
    if max_int != i:
        A[i], A[max_int] = A[max_int], A[i]
        heapify(A,n,max_int)

def build_heap(A):
    n = len(A)

    for i in range(parent(n-1),-1,-1): 
        heapify(A,n,i)

def heap_sort(A):
    build_heap(A)
    n = len(A)
    for i in range(n):
        A[n-i-1], A[0] = A[n-i-1], A[0]
        heapify(A,n-i-1,0)