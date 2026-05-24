def solve(E:list):
    n = len(E)
    dp = [[float('inf')]*n for _ in range(n)] # dynamik ilosc energi x ilosc skokow
    dp[0][E[0]] = 0  
    dp[0][0] =0 

    for i in range(0, n):
        for j in range(0,n):
            if dp[i][j] == float('inf'): 
                continue
        
            for e in range(1, j+1): 
                # e to kazdy mozliwy skok od 1 do j
                if i + e >= n: continue
                # obliczamy ile mamy teraz energii 
                nowa_e = min(n-1, j-e+E[i+e])
                # obliczamy dp czyli na nowym miejscu albo skok z porzedniego +1 jest mniejszy albo to miejsce ma juz mniejsze
                dp[i+e][nowa_e] = min(dp[i+e][nowa_e], dp[i][j]+1)

    
    if min(dp[n-1]) == float('inf'): return -1 
    return min(dp[n-1]) # zwracamy minimalny wynik z ostatniego pola

# ==========================================
# PROSTA TESTERKA
# ==========================================
def testuj_zabe():
    testy = [
        # Format: (tablica_przekąsek, oczekiwana_liczba_skokow)
        
        # Test 1: Żaba jest już na miejscu docelowym (0 skoków)
        ([0], 0),
        
        # Test 2: Standardowy skok o 1 pole
        ([1, 0], 1),
        
        # Test 3: Brak energii na start, żaba nie może się ruszyć
        ([0, 5], -1),
        
        # Test 4: Żaba musi skakać po 1 polu, bo zjada tylko po 1 energii
        ([1, 1, 1, 0], 3),
        
        # Test 5: Bardziej opłaca się skoczyć od razu o 2 pola, 
        # a potem z indeksu 2 skoczyć na indeks 3.
        ([2, 0, 1, 0], 2),
        
        # Test 6: Żaba ma od razu wystarczająco energii na gigantyczny skok
        ([3, 0, 0, 0], 1),
        
        # Test 7: Żaba ma energię na start na skok o 2, ląduje na zerze 
        # i nie ma jak doskoczyć do końca (brakuje energii).
        ([2, 0, 0, 0], -1),
        
        # Test 8: Trochę dłuższa trasa. 
        # Trasa: 0 -> 1 -> 3 -> 4 (czyli skoki o 1, o 2, o 1).
        ([1, 2, 0, 1, 0], 3)
    ]
    
    print("Rozpoczynam testy Głodnej Żaby...\n" + "-"*40)
    
    zaliczono = 0
    for nr, (A, oczekiwany_wynik) in enumerate(testy, 1):
        # Kopiujemy tablicę, w razie gdyby Twój algorytm ją modyfikował
        twoj_wynik = solve(A.copy())
        
        if twoj_wynik == oczekiwany_wynik:
            print(f" ✅ Test {nr} DOBRZE! Wynik: {twoj_wynik}")
            zaliczono += 1
        else:
            print(f" ❌ Test {nr} ŹLE! Dla planszy {A}")
            print(f"    Oczekiwano: {oczekiwany_wynik}, a Twój algorytm zwrócił: {twoj_wynik}")
            
    print("-" * 40)
    print(f"Wynik końcowy: {zaliczono} / {len(testy)} testów zaliczonych.")

if __name__ == "__main__":
    testuj_zabe()