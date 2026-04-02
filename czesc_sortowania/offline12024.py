class Node:
    def __init__(self):
        self.val = None
        self.next = None

def left(i):
    return (i*2)+1
def right(i):
    return (i*2)+2
def parent(i):
    return (i-1)//2

def heapify(A, n, i):
    max_int = i

    if left(i) < n and A[max_int] < A[left(i)]: 
        max_int = left(i)

    if right(i) < n and A[max_int] < A[right(i)]: 
        max_int = right(i)

    if max_int!=i:
        A[i], A[max_int] = A[max_int], A[i]
        heapify(A,n,max_int)

def heap_sort(A):
    n = len(A)

    for i in range(parent(n-1), -1, -1):
        



def solve(p,k):
    ...