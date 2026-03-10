""""Mamy n norek norki sa postaci krotek (a1,b1), (a2,b2), (a3,b3), (a4,b4),...,(an,bn)
    wiemy ze zachodzi a1<b1<a2<b2<....an<bn, mamy k chomikow chomiki moga byc obok siebie
    ale chcialyby byc jak najdalej. Znajdz najkrotsza odleglosc miedzy dwoma chomikami taka
    ze sa najbardziej daleko od siebie jak sie da"""


"""
Opis algortymu:

O(nlog(n))

Uzywamy binary searcha po wyniku do szukania mozliwych odleglosci pomiedzy chomikami 
szuakmy od 1 (zakladam ze chomiki nie sa na sobie) do bn-a1 
(nie moga byc dalej od siebie niz wynosi ta odlegosc), funkcja pomocicza check
sprawdza czy dla danego middle w binary seachu(m), ktory jest minimalna odlegloscia pomiedzy
chomikami da sie je rozstawic

"""

def check(norki: list[tuple], min_dist: int, k: int) -> bool:

    prev_pos = norki[0][0] # dajemy pierwszego chomika na pierwsze miejsce, bo sie to napewno oplaca
    k-=1 

    for norka in norki:
        if prev_pos + min_dist > norka[1]:
            continue
        while prev_pos + min_dist <= norka[1]:
            prev_pos = max(norka[0], prev_pos+min_dist)
            if prev_pos >= norka[0]:
                k-=1
            if k==0:
                return True
    return False 


def binary_search(norki: list[tuple], k: int) -> int:
    
    first = norki[0][0]
    n = len(norki)
    last = norki[n-1][1]
    dist = last - first
    
    l,r = 1,dist
    ans = 0

    while l<=r:
        m = (l+r)//2

        # mozemy obsadzic chomiki w norkach w takiej odleglosci
        if check(norki, m, k) == True:
            l = m+1
            ans = m
        
        else:
            r = m-1

    return ans


if __name__ == "__main__":

    norki = [(10, 20), (30, 40)]
    k = 4
    ans = binary_search(norki, k)
    print(ans)