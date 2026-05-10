def solve(klocki: list):

    n = len(klocki)
    dp = [1]*n

    for i in range(n): 
        for j in range(n):
            if i == j: continue
            if klocki[i][0] <= klocki[j][0] and klocki[i][1] >= klocki[j][1]: 
                dp[j] = max(dp[j], dp[i]+1)
    
    return n - dp[n-1]

# ==========================================
# PROSTA TESTERKA
# ==========================================
def testuj_klocki():
    testy = [
        # Format: (lista_klocków, oczekiwany_wynik_czyli_ile_usunac)
        
        # Test 1: Idealna wieża, każdy kolejny klocek jest mniejszy. (Usuwamy 0)
        ([[0, 10], [1, 9], [2, 8]], 0),
        
        # Test 2: Żaden klocek nie pasuje do poprzedniego. 
        # Najwyższa wieża ma 1 klocek. (Usuwamy 2)
        ([[0, 2], [3, 5], [6, 8]], 2),
        
        # Test 3: Klasyczna pułapka na "zachłana" (ten przykład, o którym rozmawialiśmy).
        # Bierzemy [0, 100], [1, 99], [2, 98]. Odrzucamy [45, 55]. (Usuwamy 1)
        ([[0, 100], [45, 55], [1, 99], [2, 98]], 1),
        
        # Test 4: Identyczne klocki.
        # Zawsze się na sobie mieszczą. (Usuwamy 0)
        ([[5, 10], [5, 10], [5, 10]], 0),
        
        # Test 5: Większy, mieszany przypadek.
        # Optymalna wieża: [0, 20] -> [2, 18] -> [4, 15] -> [5, 14] (4 klocki)
        # Klocki do usunięcia: [5, 25] (wystaje) oraz [1, 10] (zepsułoby dalsze układanie).
        # Z 6 klocków wyrzucamy 2. (Usuwamy 2)
        ([[0, 20], [5, 25], [2, 18], [1, 10], [4, 15], [5, 14]], 2)
    ]
    
    print("Rozpoczynam testy Spadających Klocków...\n" + "-"*40)
    
    zaliczono = 0
    for nr, (klocki, oczekiwany_wynik) in enumerate(testy, 1):
        print(f"Test {nr} | Klocki: {klocki}")
        
        twoj_wynik = solve(klocki)
        
        if twoj_wynik == oczekiwany_wynik:
            print(f" ✅ DOBRZE! Liczba klocków do usunięcia: {twoj_wynik}")
            zaliczono += 1
        else:
            print(f" ❌ ŹLE! Twój algorytm kazał usunąć {twoj_wynik} klocków, a prawidłowa odpowiedź to {oczekiwany_wynik}.")
            
        print("-" * 40)
        
    print(f"Wynik końcowy: {zaliczono} / {len(testy)} testów zaliczonych.")

if __name__ == "__main__":
    testuj_klocki()