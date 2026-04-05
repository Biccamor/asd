class Node:
    def __init(self,val,next=None):
        self.val = val
        self.next = next

def left(i):
    return (i*2)+1
def right(i):
    return (i*2)+2
def parent(i):
    return (i-1)//2

def heapify(A, i,n):
    min_int = i

    if left(i[0]) < n and A[left(i[0])][0] < A[i][0]:
        min_int = A[left(i[0])]
    if right(i[0]) < n and A[right(i[0])][0] < A[i[0]][0]:
        min_int = A[right(i[0])]    

    if min_int != i:
        A[min_int], A[i] = A[i], A[min_int]
        heapify(A,min_int,n)

def create_heap(A):
    n = len(A)
    