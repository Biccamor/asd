def parent(i):
      return (i-1)//2
def left(i):
      return (i*2)+1 
def right(i):
      return (i*2)+2

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

def heapify_max(A,n,i):
    
    max_int = i
    if left(i) < n and A[left(i)] > A[max_int]:
        max_int = left(i)

    if right(i) < n and A[right(i)] > A[max_int]: 
          max_int = right(i)
    
    if max_int != i: 
          A[i], A[max_int] = A[max_int], A[i]
          heapify_max(A,n,max_int)

def heapify_min(A,n,i):
    min_int = i

    if left(i) < n and A[left(i)] < A[min_int]:
         min_int = left(i)

    if right(i) < n and A[right(i)] < A[min_int]:
         min_int = right(i)

    if min_int != i:
         A[i], A[min_int] = A[min_int], A[i]
         heapify_min(A,n,min_int)
   

def delete_max(A):
    if len(A)==0: return None
    if len(A)==1: return A.pop()
    A[0] = A[-1]
    A.pop()
    heapify_max(A,len(A), 0)

def delete_min(A):
     if len(A) == 0: return None
     if len(A) == 1: A.pop()
     A[0] = A[-1]
     A.pop()
     heapify_min(A,len(A), 0)

if __name__ == "__main__":
    A = [60, 50, 30, 20, 15, 10, 8, 16]
    delete_max(A)
    print(A)

    B = [3,6,10,8,11,14,160]
    delete_min(B)
    print(B)