"""
Dana jest n-elementowa tablica liczb naturalnych T. Dla każdego indeksu i < n, rangą elementu
na pozycji i określamy liczbę elemen
"""

def merge(A,B,ranks,p,q,r):
    i = p
    j = q
    k = p 

    while i < q and j < r:

        if A[i][0] < A[j][0]: 
            B[k] = A[i]
            i+=1
            ranks[A[j][1]] += (i - p)

        else:
            B[k] = A[j]
            j+=1
        k+=1

    while i<q:
        B[k] = A[i]
        i+=1
        k+=1 

    while j<r:
        B[k] = A[j]
        j+=1
        k+=1

    for t in range(p,r):
        A[t] = B[t]
    

def merge_sort(A,B,ranks,p,r):
    
    if r - p <= 1: return 

    q = (p+r)//2

    merge_sort(A,B,ranks,p,q)
    merge_sort(A,B,ranks,q,r)
    merge(A,B,ranks,p,q,r)

def convert(A,n):

    for i in range(n):
        akt = A[i]
        A[i] = (akt, i)

def max_rank(A):
    n = len(A)
    B = [(0,0)]*n
    ranks = [0]*n
    convert(A,n)
    merge_sort(A,B,ranks,0,n)
    print(ranks)
    print(A)
if __name__ == "__main__":
    
    A = [5,3,9,4]
    max_rank(A)