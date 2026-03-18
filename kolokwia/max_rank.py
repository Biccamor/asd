"""
Dana jest n-elementowa tablica liczb naturalnych T. Dla każdego indeksu i < n, rangą elementu
na pozycji i określamy liczbę elementów, które w tablicy występują przed elementem i-tym, a ich
wartość jest mniejsza od T[i].
"""

""""
Opis algorytmu:
jest to modyfikacja algorytmu sortowania merge_sort
liste elementow zamienamiy na liste krotek gidze drugi element to indeks pierwszy wartosc oraz tworzymy
tablice ranks odpowiedzialna za zliacznie rangi dla danego elementu w czym ulatwia trzymanie indeksu

range zliczamy w funkcji merge za kazdym razem gdy element z pierwszej czesci obecnie mergowanych czesci tablicy
jest wiekszy niz drugi, dlatego ze to oznacza
"""


def merge(A: list, B: list, ranks: list, p: int, q: int, r: int):
    
    i = p
    j = q
    k = p

    while i<q and j<r:

        if A[i][0] < A[j][0]: # tak jak "powinno" byc tzn najpierw lewy potem prawy
            
            B[k] = A[i]
            i+=1
        
        else:
            B[k] = A[j]
            ranks[A[j][1]] += i - p
            j+=1

        k+=1

    while i<q:
        B[k] = A[i]
        i+=1
        k+=1

    while j<r:
        B[k] = A[j]
        ranks[A[j][1]] += i - p
        j+=1
        k+=1

    for t in range(p,r):
        A[t] = B[t]
        

def merge_sort(A: list,B: list,ranks: list,p: int ,r: int):
    if r-p <= 1: return 
    
    q = (p+r)//2
    merge_sort(A,B,ranks,p,q) #left
    merge_sort(A,B,ranks,q,r) # right
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
    
    A = [10,11,15,3,4,5]
    max_rank(A)