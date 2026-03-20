class Heap:

    def __init__(self, A):
        self.A = A
        self.max_heap = [[el,i]for i, el in enumerate(self.A)]
        self.min_heap = [[el,i] for i, el in enumerate(self.A)]
        self.build_heap_max()
        self.build_heap_min()

    def parent(self,i):
        return (i-1)//2

    def left(self,i):
        return (i*2)+1
    def right(self,i):
        return (i*2)+2

    def insert(self,i):
        self.insert_max(i)
        self.insert_min(i)

    def insert_max(self, i):
        n = len(self.max_heap)
        self.max_heap.append([i,n])
        n +=1
        idx = n-1
        while idx > 0 and i > self.max_heap[self.parent(idx)][0]:
            p_idx = self.parent(idx)
            [i,idx], self.max_heap[p_idx] = self.max_heap[p_idx], [i,idx]
            idx = p_idx

    def insert_min(self,i):
        n = len(self.min_heap)
        self.min_heap.append([i,n])
        n+=1
        idx = n-1
        while idx > 0 and i < self.min_heap[self.parent(idx)][0]:
            p_idx = self.parent(idx)
            [i,idx], self.min_heap[p_idx] = self.min_heap[p_idx], [i,idx] 
            idx = p_idx

    def heapify_max(self,n,i):
        max_int = i 

        if self.left(max_int) < n and self.max_heap[max_int][0] < self.max_heap[self.left(i)][0]:
            max_int = self.left(i)

        if self.right(max_int) < n and self.max_heap[max_int][0] < self.max_heap[self.right(i)][0]:
            max_int = self.right(i)
        
        if max_int != i:

            self.heapify_max(n,max_int)


    def heapify_min(self,n,i):
        min_int = i 

        if self.left(min_int) < n and self.min_heap[min_int][0] > self.min_heap[self.left(i)][0]:
            min_int = self.left(i)

        if self.right(min_int) < n and self.min_heap[min_int][0] > self.min_heap[self.right(i)][0]:
            min_int = self.right(i)
        
        if min_int != i:
            self.swap_min(min_int,i)
            self.heapify_min(n,min_int)

    def delete_max(self,n):
        
        if len(self.max_heap) == 0: return None
        if len(self.max_heap) == 1: return self.max_heap.pop()
        max_el = self.max_heap[0]
        self.min_heap[max_el[1]] = self.min_heap[-1]
        self.heapify_min(n,max_el[1])


        self.max_heap[0] = self.max_heap[-1]
        self.max_heap.pop()
        self.heapify_max(n,0)
        

    def delete_min(self,n):
        
        if len(self.min_heap) == 0: return None
        if len(self.min_heap) == 1: return self.min_heap.pop()
        
        min_el = self.min_heap[0]
        self.min_heap[min_el[1]] = self.max_heap[-1]
        self.heapify_min(n,min_el[1])

        self.min_heap[0] = self.min_heap[-1]
        self.min_heap.pop()

        self.heapify_min(n,0)


    def build_heap_max(self): 
        n = len(self.max_heap)
        for i in range(self.parent(n-1), -1, -1):
            self.heapify_max(n,i)

    def build_heap_min(self):
        n = len(self.min_heap)
        for i in range(self.parent(n-1), -1,-1):
            self.heapify_min(n,i)
        

    def swap_max(self,i,j):
        
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]


        self.min_heap[self.max_heap[i][1]] = self.max_heap[j][1]
        self.min_heap[self.max_heap[j][1]] = self.max_heap[i][1]

    def swap_min(self,i,j):
        
        self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]


        self.max_heap[self.min_heap[i][1]] = self.min_heap[j][1]
        self.max_heap[self.min_heap[j][1]] = self.min_heap[i][1]