"""
A = [1, ... , n] <- posortowana rosnaco/niemalejaco
sprawdz czy dla podanego x istnieje A[i]+A[j]=x

"""


"""
Opis algorytmu:
O(n) wytłumaczenie: przechodimy raz po tablicy (dlugosci n) dwoma wskaznikami przejda lacznie 
w pesymsycznym scenariuszu raz tablice 

Tworzymy dwa wskazniki jeden wskazuje dla poczatku drugi dla konca tablicy
sprawdzamy dla wskaznikow czy ich wartosci w tablicy daja x
jak tak to zwarcamy jak jest za duzo to zabieramy z prawego(wiekszej liczby)
jak za malo to idziemy lewym do przodu

"""


def solve(tab: list[int], x: int) -> tuple[int, int] | None:
    l,r = 0, len(tab)-1

    while l<r:

        if tab[l] + tab[r] == x:
            return (l,r)
        
        if tab[l] + tab[r] > x:
            r -= 1
        else:
            l+=1

    return None            



if __name__=="__main__":
    tab = [1,3,4,5,7,8,12,20,30]
    x = 12
    ans= solve(tab,x)
    if ans == None:
        print("BRAK")
    
    else:
        print(f"i: {ans[0]}, {tab[ans[0]]}  j: {ans[1]}, {tab[ans[1]]}")