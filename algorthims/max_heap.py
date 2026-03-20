def parent(i):
    # Poprawiony wzór dla tablic zaczynających się od indeksu 0
    return (i - 1) // 2

def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2

def heapify(A, n, i):
    """
    A - tablica/kopiec 
    n - ilosc liczb w tablicy
    i - akutalny element w kopcu ktory chcemy dac na dobre miejsce
    """
    max_idx = i
    if left(i) < n and A[left(i)] > A[max_idx]:
        max_idx = left(i)
    if right(i) < n and A[right(i)] > A[max_idx]:
        max_idx = right(i)
    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        heapify(A, n, max_idx)

def build_heap(A):
    n = len(A)
    # Zaczynamy od ojca ostatniego elementu i idziemy do 0
    for i in range(parent(n - 1), -1, -1): 
        heapify(A, n, i)