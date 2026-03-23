import sys

def left(i):
    return (i*2)+1
def right(i):
    return (i*2)+2
def parent(i):
    return (i-1)//2

sys.setrecursionlimit(500000)

def heapify(A: list, n: int, i: int):

    max_int = i

    if left(i) < n and A[left(i)] > A[max_int]:
        max_int = left(i)

    if right(i) < n and A[right(i)] > A[max_int]:
        max_int = right(i)
        
    if max_int != i:
        A[i], A[max_int] = A[max_int], A[i]
        heapify(A,n,max_int)

def create_heap(A):
    n = len(A)
    if n < 2: return A 

    for i in range(parent(n-1), -1,-1):
        heapify(A, n, i)
def solve(A, B):
    
    create_heap(A)
    create_heap(B)

    n = len(A)
    for i in range(n):
        A[n-i-1], A[0] = A[0],  A[n-i-1]
        heapify(A,n-i-1,0)

        B[n-i-1], B[0] =  B[0], B[n-i-1]
        heapify(B,n-i-1,0)


    akt = 1
    ans = [1, A[0]]
    start = 1 
    end = 0
    #print(A)
    #print(B)
    while start < n:

        if A[start] <= B[end]: 
            akt +=1 
            start +=1 
        else:
            end+=1
            akt -=1 

        if ans[0] < akt:
            ans = [akt, A[start-1]]

    return ans

def get_input():
    for line in sys.stdin:
        for word in line.split():
            yield int(word)

if __name__ == "__main__":

    input_gen = get_input()
    L = []
    H =[]
    try:
        n = next(input_gen)
        t_val = next(input_gen)
        
        for _ in range(n):
            l = next(input_gen)
            h = next(input_gen)
            L.append(l)
            H.append(h)
            
        if L and H:
            ans = solve(L, H)
            print(f"{ans[0]} {ans[1]}")
        else:
            pass 

    except (StopIteration, ValueError):
        if L and H:
            ans = solve(L,H)
            print(f"{ans[0]} {ans[1]}")