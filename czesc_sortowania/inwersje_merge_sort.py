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
            inv_count += (q-i)
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
    return inv_count

def merge_sort(A: list, B: list, p: int, r: int):
    
    if r-p <=1: return 0# jezeli miedzy startem a koncem jest tylko 1 element lub 0 to zwracamy odrazu

    q = (r+p)//2 # ustawiamy srodek
    left_inv = merge_sort(A,B,p,q) # inwersje ktore sa w lewej czesci tablicy podczas jej sortowania
    right_inv = merge_sort(A,B,q,r) # inwersje ktore sa w prawej czesci tablicy podczas jej sortowania
    split_inv = merge(A,B,p,q,r) # inwersje podczas laczenie dwoch tablic
    return left_inv+right_inv+split_inv

def main(A: list):
    n = len(A)
    B = [0]*n
    inv = merge_sort(A,B,0,n)
    return inv

if __name__ == "__main__":
    A = [0,4,53,3,9,18,17,3,1]
    inv = main(A)
    print(A)
    print(f"number of inv {inv}")