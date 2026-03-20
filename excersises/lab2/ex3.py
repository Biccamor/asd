def parent(i):
    return (i-1)//2
def left(i):
    return (i*2)+1
def right(i):
    return (i*2)+2


def heapify(A,n,i):
    
    max_int = i

    if left(i) < n and A[max_int] < A[left(i)]:
        max_int = left(i)
    if right(i) < n and A[max_int] < A[right(i)]:
        max_int = right(i)
    
    if i!=max_int:
        heapify(A,n,max_int)

def create_heap(A):
    n = len(A)

    for i in range(parent(n-1), -1, -1):
        heapify(A,n,i)

def insert(A,i):
    """
    Wstawiamy na 
    """
    A.append(i)
    idx = len(A)-1
    print(A[parent(idx)])
    while A[parent(idx)] < i and idx > 0:
        p_idx = parent(idx)
        A[p_idx], A[idx] = A[idx], A[p_idx]
        idx = p_idx


if __name__=="__main__":
    
    A = [50,40,30,25,15,20,10]
    create_heap(A)
    insert(A,42)
    print(A)