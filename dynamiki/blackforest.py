def solve(C:list): 
    n = len(C)
    dp = [0]*(n+1)
    dp[0] = C[0]
    dp[1] = max(C[0], C[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2]+C[i])

    return dp[n-1]

# ==========================================
def proste_testy():
    # Lista testów w formacie: (tablica_drzew, oczekiwany_maksymalny_zysk)
    testy = [
        ([5, 10], 10),           # Bierzemy tylko 10 (indeks 1)
        ([1, 2, 3, 1], 4),       # Bierzemy 1 (indeks 0) i 3 (indeks 2)
        ([2, 7, 9, 3, 1], 12),   # Bierzemy 2 (ind. 0), 9 (ind. 2) i 1 (ind. 4)
        ([2, 1, 1, 2], 4)        # Bierzemy 2 (ind. 0) i 2 (ind. 3)
    ]
    
    print("Odpalam proste testy...\n" + "-"*40)
    
    for nr, (tablica, oczekiwany_zysk) in enumerate(testy, 1):
        print(f"Test {nr} | Tablica drzew: {tablica}")
        
        # Wywołujemy Twój algorytm
        twoj_zysk = solve(tablica)
        
        # Sprawdzamy, czy zysk się zgadza
        if twoj_zysk == oczekiwany_zysk:
            print(f" ✅ DOBRZE! Obliczony zysk: {twoj_zysk}")
            #print(f"    Twój plan wycinki (indeksy): {twoj_plan}")
        else:
            print(f" ❌ ŹLE! Obliczony zysk to {twoj_zysk}, a powinno wyjść {oczekiwany_zysk}.")
            #print(f"    Twój plan wycinki (indeksy): {twoj_plan}")
            
        print("-" * 40)

if __name__ == "__main__":
    proste_testy()