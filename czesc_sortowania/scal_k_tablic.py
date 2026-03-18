"""
Mamy k posortowanych tablic chcemy je zlaczyc
"""
def left(i):
    return i*2+1
def right(i):
    return i*2+2
def parent(i):
    return (i-1)//2

"""Tworzymy min heapa"""

def heapify(A,n,i):

    max_int = i

    if left(i) < n and A[max_int] > A[left(i)]:
        max_int = left(i)

    if right(i) < n and A[max_int] > A[right(i)]:
        max_int = right(i)

    if i != max_int:
        A[i], A[max_int] = A[max_int], A[i]
        heapify(A,n,max_int)


def create_heap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)


def solve(listy: list[list]):
    """
        trzmyamy w kopcu po jednej wartosci z kazdej listy i znajdujemy minimum w czasie O(Logp) gdzie p to ilosc list
        najmniejsza wartocs dajemy na liste wynikowa a zamiast niej dajemy kolejny element Z JEJ LISTY
        jezeli lista sie skonczyla to przerzucamy element ostatni na pierwsze miejsce (bo je juz wrzucilismy na wynik)
        i robimy heapify pokolei zrzucajac elementy jak sie skonczy heap to konczymy petle i zwracamy tablice wynikowa
        dziala to jak kolejka priorytetowa

    """  
    heap = [] # pierwsze miejsca z ktorym buduhjemy najpierw kopiec

    for nr_listy, lista in enumerate(listy):
        if len(lista)>0: 
            heap.append((lista[0], nr_listy,0))

    ans_list = [] # tablica w ktorej trzymamy ostateczny wynik
    create_heap(heap)

    while True:

        akt_val, akt_list, akt_idx = heap[0]
        ans_list.append(heap[0][0])

        akt_idx+=1 
        if akt_idx < len(listy[akt_list]):
            heap[0] = (listy[akt_list][akt_idx], akt_list, akt_idx)
        else:
            akt = heap.pop()
            if len(heap)>0:
                heap[0] = akt

        if len(heap)>0:
            heapify(heap,len(heap),0)
        
        else: 
            break

    return ans_list

def wczytaj(*kolejki):
    lista = []
    n = len(kolejki)
    for i in range(n):
        lista.append(kolejki[i])
    return lista

if __name__ == "__main__":
    A = [1, 4, 5, 8, 9]
    B = []
    C = [2, 2, 6]
    D = [0, 10]
    lista = wczytaj(A,B,C,D)
    ans = solve(lista)
    print(ans)