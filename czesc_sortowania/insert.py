def parent(i):
    return (i-1)//2

# max heap 

def insert_max_heap(A,i):
    
    A.append(i)
    idx = len(A)-1
    while idx >0 and A[parent(idx)] < A[idx]:
            p_idx = parent(idx)
            A[p_idx], A[idx] = A[idx], A[p_idx]
            idx = p_idx

def insert_min_heap(A,i):
    A.append(i)
    idx = len(A)-1

    while idx >0 and A[parent(idx)] > A[idx]:
            p_idx = parent(idx)
            A[p_idx], A[idx] = A[idx], A[p_idx]
            idx = p_idx


if __name__ == "__main__":

    A = [50, 30, 20, 15, 10, 8, 16]
    i = 60
    insert_max_heap(A,i)
    print(A)