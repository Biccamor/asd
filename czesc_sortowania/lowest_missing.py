"""
Mamy tablicę A = [a0, ..., an-1] posortowaną rosnąco i wypełnioną liczbami od [0, ..., n - 1].
Na każdym indeksie powinna być odpowiadająca mu wartość, czyli A[i] = i, ale niestety tak nie jest.
W pewnym momencie ten porządek jest zaburzony.
Musimy znaleźć najmniejszą liczbę, której nie ma w tablicy, czyli tę, której
indeks jest różny od wartości.
"""

def binary_search(A: list[int]) -> int:

    l,r = 0, len(A)-1

    while l<=r:
        m = (l+r)//2
        if A[m]==m:
            l = m+1
        else:
            r = m-1
    return l
        

if __name__ == "__main__":
    A = [0, 1,2,4,5,6, 11, 12]
    print(binary_search(A))