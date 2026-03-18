"""
Znalezc k najwiekszych elementow
"""

def left(i):
    return i*2+2
def right(i):
    return i*2+1
def parent(i):
    return (i-1)//2

def heapify(A,n,i):
    min_int = i 

    if left(i)<n and A[min_int] > A[left(i)]:
        min_int = left(i)
    if right(i)<n and A[min_int] > A[right(i)]:
        min_int = right(i)
    if min_int != i:
        A[min_int], A[i] = A[i], A[min_int]
        heapify(A,n,min_int)

def create_heap(A):
    n = len(A)

    for i in range(parent(n-1), -1, -1):
        heapify(A,n,i)

def solve(A, k):
    heap = []
    for i in range(0,k):
        heap.append(A[i])

    create_heap(heap) # tworzymy min heapa ktory trzyma k najwiekszych wartosci

    for i in range(k, len(A)):
        if heap[0] < A[i]: 
            heap[0] = A[i]
            heapify(heap,len(heap),0)
        
    print(heap)

if __name__ == "__main__":
    A = [1,5,7,3,10,14,2,8,120,0,10,15,3,8,9,22]
    k = 4
    solve(A,k)