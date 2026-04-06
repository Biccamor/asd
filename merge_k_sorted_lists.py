class Node:
    def __init__(self,val=None,next=None):
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

    if left(min_int) < n and A[left(i)][0] < A[min_int][0]:
        min_int = left(i)
    if right(min_int) < n and A[right(i)][0] < A[min_int][0]:
        min_int = right(i)   

    if min_int != i:
        A[min_int], A[i] = A[i], A[min_int]
        heapify(A,min_int,n)

def create_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A,i,n)

def add(A,i,l_num, idx):
    A.append((i, l_num, idx))
    n = len(A)
    idx = n-1
    while idx > 0 and A[idx][0] < A[parent(idx)][0]:
        A[idx], A[parent(idx)] = A[parent(idx)], A[idx]
        idx = parent(idx)

def pop_min(A):
    min_val = A[0]
    A[0] = A[-1]
    A.pop()
    n = len(A)
    heapify(A,0,n)
    return min_val
    
def solve(lists):

    if len(lists) == 0: 
        return
    
    heap = [] 
    
    for l in range(len(lists)):
        add(heap, lists[l][0], l, 0)
    create_heap(heap)

    head = Node()
    ans = head
    ans.val = None
    
    while len(heap) != 0:
        min_val = pop_min(heap)
        ans.next = Node(min_val[0])
        ans = ans.next
        if len(lists[min_val[1]])-1 >= min_val[2]+1:
            add(heap, lists[min_val[1]][min_val[2]+1], min_val[1], min_val[2]+1)


    return head.next


if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    ans = solve(lists)  
    while ans != None:
        print(ans.val)
        ans = ans.next