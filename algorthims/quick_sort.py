def partition(l,h,A) -> int:

    """
    Funckja do szukania miejsca partycji -> divide and conquer 
    ustawiamy pivot na poczatke i szukamy poprzez porownania gdzie powinnien byc dany element czesc 1 jest przed
    tym elementem i elementy w niej trzeba posortowac po prawej czesci tez sa elementy ktore maja sie znajdowac
    poprzez zamianieani lewej i prawej czesci ta czesc tez tzreba posortowac

    funckja partition sluzy tylko do znaleznia pivotu
    """

    pivot = A[l]
    i, j = l, h-1

    while i<j: 

        while A[i] <= pivot and i < h-1:
            i+=1
        while A[j] > pivot and j > 0:
            j-=1
        
        if i < j:
            A[i], A[j] = A[j],A[i]

    A[l], A[j] = A[j], A[l]
    return j


def quick_sort(l,h,A):
    if h-l < 2: return 

    j = partition(l,h,A)
    quick_sort(l,j,A) #left
    quick_sort(j+1,h,A) # right


if __name__ == "__main__": 
    A = [10,4,5,31,6,17,2,1,14,38]
    quick_sort(0,len(A),A)
    print(A)