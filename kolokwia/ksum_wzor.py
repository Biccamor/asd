class minHeap:

    def __init__(self):
        self.A = []
        self.suma = 0

    def parent(self,i):
        return (i-1)//2

    def left(self,i):
        return(i*2)+1
    def right(self,i):
        return (i*2)+2

    def heapify(self,i,n):
        min_idx = i

        if self.left(min_idx) < n-1 and self.A[self.left(min_idx)][0] < self.A[min_idx][0]:
            min_idx = self.left(min_idx)

        if self.right(min_idx) < n-1 and self.A[self.right(min_idx)][0] < self.A[min_idx][0]:
            min_idx = self.right(min_idx)

        if min_idx!=i:
            self.A[min_idx], self.A[i] = self.A[i], self.A[min_idx]
            self.heapify(min_idx,n)
 

    def add(self, i):
        self.A.append(i)
        self.suma += i[1]
        n = len(self.A)
        idx  = n-1

        while idx > 0 and self.A[self.parent(idx)][0] > self.A[idx][0]:
            self.A[idx],self.A[self.parent(idx)] = self.A[self.parent(idx)], self.A[idx]
            idx = self.parent(idx)

    def pop_min(self):
        
        self.suma -= self.A[0][1]
        self.A[0] = self.A[-1]
        self.A.pop()
        n = len(self.A)
        self.heapify(0,n)

        

def solve(T,k,p):
    
    heap = minHeap()
    for i in range(0,p):
        heap.add([i, T[i]])
    ans = 0
    ans += heap.suma
    n = len(T)
    i = 1 
    j = p+1 
    while j < n:
        heap.pop_min()
        heap.add((i,T[i]))
        ans += heap.suma