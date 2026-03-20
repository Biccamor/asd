""""
1 2 3 1 2 3 4 3 4 2 5
"""
""""
idziemy gasienica sliding window trzymamy tablice kolorow ktore maja 0 lub 1
jezeli jest 1 to byl jak 0 to nie byl i trzymamy w zmiennej ile obecnie jest w uzyciu kolorow, oraz nasz wynik

sprawdzamy czy jest zero jezeli tak to wtedy zamienami na jeden idziemy j do przodu i dodajemy do count +1
jezeli jest 1 to nic nie robimy
jezeli count == k (wszysktie kolory)
to sprawdzamy wynik czy jest mniejszt niz ostatnio
i usutawmy kolory[A[i]]
i idzemy i do prozdu
"""
def kolory(A,k):
    
    i = 0
    j = 1
    kolory = [0]*k
    n = len(A)
    ans = float('inf')
    kolory[A[i]] += 1 
    count_akt = 1
    while j<n:
        
        if kolory[A[j]] == 0:
            kolory[A[j]] += 1
            count_akt += 1

        if count_akt == k: 
            ans = min(ans, count_akt)
            kolory[A[i]] = 0
            i+=1
 
        j+=1

    return ans