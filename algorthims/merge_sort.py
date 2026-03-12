def merge(A: list ,B: list, p: int, q: int, r: int):
    
    """
    tablica A: tablica ktora chcemy posortowac
    tablica B: buffor/tablica pomocnicza
    p - start pierwszej czesci
    q -  start drugiej czesci
    r - koniec calej tablicy
    """

    i = p # wskaznik na akt miejsce w 1 czesci
    j = q # wskaznik na akt miejsce w 2 czesci
    k = p # aktualne miejsce w naprawianej temp (B) tablicy
    inv_count = 0

    while i < q and j <r:

        if A[i] <= A[j]:
            B[k] = A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1
        k+=1
    
    # jezeli zostana z 1 czesci
    while i<q:
        B[k] = A[i]
        i+=1
        k+=1

    # jezeli zostana z 2 czesci
    while j<r:
        B[k] = A[j]
        j+=1
        k+=1

    for t in range(p,r): # od poczatku tablicy do konca
        A[t] = B[t] # naprawiamy prawdziwa tablice

def merge_sort(A: list, B: list, p: int, r: int):
    
    if r-p <=1: return # jezeli miedzy startem a koncem jest tylko 1 element lub 0 to zwracamy odrazu

    q = (r+p)//2 # ustawiamy srodek
    merge_sort(A,B,p,q)
    merge_sort(A,B,q,r)
    merge(A,B,p,q,r)

def main(A):
    n = len(A)
    B = [0]*n
    merge_sort(A,B,0,n)

if __name__ == "__main__":
    A = [0,4,53,3,9,18,17,3,1]
    main(A)
    print(A)