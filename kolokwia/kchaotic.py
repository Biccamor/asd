class Node:
    def __init__(self,val=None, next=None ) -> None:
        self.val = val
        self.next = next 

class minHeap:

    def __init__(self) -> None:
        self.A = []

    def left(self, i):
        return (i*2)+1
    
    def right(self, i):
        return (i*2)+2
    
    def parent(self,i):
        return (i-1)//2 

    def heapify(self, i, n):
        
        min_int = i 

        if self.left(min_int) < n and self.A[min_int] > self.A[self.left(min_int)]:
            min_int = self.left(min_int)

        if self.right(min_int) < n and self.A[min_int] > self.A[self.right(min_int)]:
            min_int = self.right(min_int)

        if min_int!=i:
            self.A[min_int], self.A[i] = self.A[i], self.A[min_int]
            self.heapify(min_int,n)

    def create_heap(self):
        n = len(self.A)
        if n==1: return

        for i in range(self.parent(n-1), -1, -1):
            self.heapify(i,n)

    def add(self, i):

        self.A.append(i)
        n = len(self.A)
        idx = n-1
        while idx > 0 and self.A[idx] < self.A[self.parent(idx)]:
            self.A[idx], self.A[self.parent(idx)] = self.A[self.parent(idx)], self.A[idx]
            idx = self.parent(idx)


    def pop_min(self):

        min_val = self.A[0]
        self.A[0] = self.A[-1]
        self.A.pop()
        n = len(self.A)
        self.heapify(0,n)

        return min_val
    
def solve(head, k):
    
    heap = minHeap()
    curr = head 
    
    for _ in range(0,k+1):
        heap.add(curr.val)
        curr = curr.next 
    ans_head = Node()
    ans = ans_head
    
    while heap.A:
        min_val = heap.pop_min()
        ans.next = Node(min_val)
        ans = ans.next 
        if curr != None:
            heap.add(curr.val)
            curr = curr.next 
    return ans_head.next 

if __name__ == "__main__":
    head = Node(1, Node(0, Node(3, Node(2, Node(4, Node(6, Node(5)))))))
    k = 1

    head = solve(head, k)

    while head:
        print(head.val)
        head = head.next